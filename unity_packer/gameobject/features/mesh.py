""" Mesh Module that defines a mesh structure.

Mesh structure will be a factory that can utilize
the index buffer and typed data unity needs as part of the
rendering environment.

This will actually link a meshfilter which can reference the mesh object

"""
from unity_packer.gameobject.base import BaseUnity
from unity_packer.yaml.writer import GenerateYamlData
from unity_packer.yaml.format import meshyaml, meshFilterYaml

from typing import List
from struct import pack, unpack
from sys import getsizeof

class Mesh():

    def __init__(self, name: str, vertices: List[float], indices: List[int], normals: List[float]):
        self.vertices = vertices
        """ List of all Vertices in Mesh

        format:
            - [{x}, {y}, {z}, {x}, {y}, {z}]
        """

        self.indices = indices
        """ List of all indices to connect vertices

        Must be 1/3 the size of the total triangles

        format:
            - [{triangle_1_x}, {triangle_2_y}, {triangle_3_z}]
        """

        self.normals = normals
        """ List of all normals for each vertices

            - Optional
        """
        
        self.uvs = []
        """ List of all UVS in the current mesh

        Not currently supported
        """

        self.base = BaseUnity(name)

        self.meshFile = BaseUnity(f'{name}_mesh')

        self.gameobject = None


    def _generateIndexBuffer(self) -> str:
        ret = ""
        # generate str value list of unsigned short values
        # needs to be in uint 16 format
        for index in range(len(self.indices)):
            val = pack("<H", self.indices[index]).hex()
            ret = f'{ret}{val}'
        return ret

    def _generateUntypedBuffer(self) -> str:
        """ Creates a string of hex data that represents the following

            - Position (f32 x 3)
                - X
                - Y
                - Z
            - Normals (f32 x 3)
                - N1
                - N2
                - N3

        Operations:

        1. Compress postions and normals into slices for each triangle
        2. Add all traingles together and create hex format for each while adding

        Returns:
            str: Compressed Hex Data
        """

        # for python 3 appending with f format seems effective enough
        ret = "";

        # a good note is that len(verticies) === len(normals)

        # python regular float is interpreted as double precision as far as I understand
        # convert each value in vertices to f32 from generic float
        #   - c_float is 4 bytes which is what we need to eliminate extra precision

        # this should pack the data for each point into a 32 bit float
        # I attempted to unroll the loop a little at least - gpu gods help me later
        for data_slice in range(int(len(self.vertices) / 3)):
            offset = data_slice * 3
            x = pack("<f", self.vertices[offset]).hex()
            y = pack("<f", self.vertices[offset + 1]).hex()
            z = pack("<f", self.vertices[offset + 2]).hex()
            n1 = pack("<f", self.normals[offset]).hex()
            n2 = pack("<f", self.normals[offset + 1]).hex()
            n3 = pack("<f", self.normals[offset + 2]).hex()
            ret = f'{ret}{x}{y}{z}{n1}{n2}{n3}'

        return ret

    def serialize(self):
        """ Generates a dictionary of yaml defined bindings to populate the reference

        - This could also add the collision meshes?
        - that would be neat and save time

        Returns:
            Dictionary<str, str>: All of the yaml reference items in yaml.mesh
        """
        # for renderer
        data = {
            'ref_id': self.base.uuid_signed(),
            'gameobject_fileID': self.base.gameobject.base.fileReference(),
            'mesh_ref_fileID': self.meshFile.fileReference(),
        }

        mesh_filter = GenerateYamlData(data, meshFilterYaml)

        # for mesh
        bindings = {
            'name': self.meshFile.name,
            'ref_id': self.meshFile.uuid_signed(),
            'index_count': len(self.indices),
            'vertex_count': len(self.vertices),
            'm_center_x': float(0.0),
            'm_center_y': float(0.0),
            'm_center_z': float(0.0),
            'm_extent_x': float(0.0),
            'm_extent_y': float(0.0),
            'm_extent_z': float(0.0),
            'm_index_buffer': self._generateIndexBuffer(),
            'm_datasize': getsizeof(self),
            '_typlessdata': self._generateUntypedBuffer(),
        }

        # generates the full data to be inserted
        mesh_ = GenerateYamlData(bindings, meshyaml)

        return f'{mesh_}{mesh_filter}'


class Parse():
    """ This class will parse a unity defined and compressed mesh if fed by string.
    """
    @staticmethod
    def parse_data_better(mesh: str) -> list:
        slices = []
        for offset in range(int(len(mesh) / 8)):
            offset = offset * 8
            # after much testing this is certainly little endian
            slices.append(unpack('<f', bytes.fromhex(mesh[offset : (offset + 8)]))[0])
        return slices

    @staticmethod
    def parse_intoMesh(slices: list):
        vertices = []
        normals = []

        for offset in range(int(len(slices) / 6)):
            offset = offset * 6
            # print(f"Triangle - [{offset}]")
            vertices.append(slices[offset + 0])
            vertices.append(slices[offset + 1])
            vertices.append(slices[offset + 2])
            normals.append(slices[offset + 3])
            normals.append(slices[offset + 4])
            normals.append(slices[offset + 5])
        
        return vertices, normals

    @staticmethod
    def parseIndicies(index: str):
        indices = []
        for offset in range(int(len(index) / 4)):
            offset = offset * 4
            indices.append(unpack('<H', bytes.fromhex(index[offset: offset + 4]))[0])
        return indices

    @staticmethod
    def parse_mesh(m_IndexBuffer: str, _typelessdata: str):
        indices = Parse.parseIndicies(m_IndexBuffer)
        slices = Parse.parse_data_better(_typelessdata)
        vertices, normals = Parse.parse_intoMesh(slices)
        return indices, vertices, normals
