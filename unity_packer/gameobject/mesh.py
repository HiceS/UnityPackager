""" Mesh Module that defines a mesh structure.

Mesh structure will be a factory that can utilize
the index buffer and typed data unity needs as part of the
rendering environment.

This will actually link a meshfilter which can reference the mesh object

"""
from unity_packer.gameobject.base import BaseUnity
from unity_packer.gameobject.material import Material
from unity_packer.yaml.writer import GenerateYamlData
from unity_packer.yaml.format import (
    meshyaml,
    meshFilterYaml,
    meshRendererYaml,
    matBasicYaml,
)

from typing import List
from struct import pack, unpack


class Mesh:
    def __init__(
        self, name: str, vertices: List[float], indices: List[int], normals: List[float]
    ):
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

        self.material = None
        """ I could allow an individual to set this flag which would automatically create the renderer and add the mat
        """

        self.base = BaseUnity(name)
        self.gameobject = None

    def getReference(self):
        """Gets the file reference for the mesh

        Returns:
            str: formatted reference
        """
        return self.base.uuid_signed()

    def _generateIndexBuffer(self) -> str:
        ret = ""
        # generate str value list of unsigned short values
        # needs to be in uint 16 format
        for index in range(len(self.indices)):
            val = pack("<H", self.indices[index]).hex()
            ret = f"{ret}{val}"
        return ret

    def _generateUntypedBuffer(self) -> str:
        """Creates a string of hex data that represents the following

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
        ret = ""

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
            ret = f"{ret}{x}{y}{z}{n1}{n2}{n3}"

        return ret

    def serialize(self):
        """Generates a dictionary of yaml defined bindings to populate the reference

        - This could also add the collision meshes?
        - that would be neat and save time

        Returns:
            Dictionary<str, str>: All of the yaml reference items in yaml.mesh
        """
        # probably should have just been vectors
        center, extents = self.localAABBMatrix(self.vertices)

        # for mesh
        bindings = {
            "name": self.base.name,
            "ref_id": self.base.uuid_signed(),
            "index_count": len(self.indices),
            "vertex_count": len(self.vertices) / 3,
            "m_center_x": center[0],
            "m_center_y": center[1],
            "m_center_z": center[2],
            "m_extent_x": extents[0],
            "m_extent_y": extents[1],
            "m_extent_z": extents[2],
            "m_index_buffer": self._generateIndexBuffer(),
            "m_datasize": self.getDataSize(),
            "_typlessdata": self._generateUntypedBuffer(),
        }

        # generates the full data to be inserted
        mesh_ = GenerateYamlData(bindings, meshyaml)

        return f"{mesh_}"

    @staticmethod
    def localAABBMatrix(verts):
        """An AABB is essentially a masking convex box that generates the render window

         - Will derive the aabb matrix if not supplied
         - Shoud be parallelized in the future

        Args:
            verts (list[floats]): vertices list

        Returns:
            - center [x, y, z]
            - extent [x, y, z]
            center, extent
        """
        # need to calculate the center and the extents of the mesh
        # this could be done by user or by me, tbd
        # this could happen with a ton of different kinds of optimizations
        # 0: Lowest
        # 1: Highest
        # 2: middle?

        # vertices format:
        #     - [{x}, {y}, {z}, {x}, {y}, {z}]
        # maybe do this by mod 3 and take the three highest and lowest?

        # if this is calculated after untyped buffer we can just delete the ones we dont need after compute of each axis
        # that way it will also free the memory in use

        # x will be every 3rd item -2
        x = verts.copy()
        del x[3 - 1 :: 3]

        y = x.copy()
        y = y[2 - 1 :: 2]

        del x[2 - 1 :: 2]
        z = verts[3 - 1 :: 3]

        # this should technically be the difference between the lowest number and max number but testing
        # i guess if you have a center you only need the max extents in order to calculate the min extents as well
        # this would be a lot easier with numpy
        x_max = max(x)
        y_max = max(y)
        z_max = max(z)

        x_min = min(x)
        y_min = min(y)
        z_min = min(z)

        extent = [x_max, y_max, z_max]
        center = [(x_max - x_min) / 2, (y_max - y_min) / 2, (z_max - z_min) / 2]

        del x, y, z

        return center, extent
        # for now im just going to keep this way of sorting the matrix

    def getDataSize(self) -> int:
        """This is absolutely necessary for the parsing,

        my best guess is that unity parses the datasize field to initiliaze it's object array which is strange because it would be easy to derive and then populate

        How it works:
            1. it's the size of the vertices buffer
            2. im only storing the pos and normals
            3. pos = (x, y, z) - each are f32 and 4 bytes in length in hex form = (4*3) = 12
            4. normals = (n1, n2, n3) - each are f32 and 4 bytes in length in hex form = (4*3) = 12
            5. each vertex would be 24Bytes of data
            6. total data size if length of array / 3 for each vertex and multiplied by 24
            7. This is equivalent to saying that each item is a 2xf32 and 8 bytes in size multiplied by the number of items
        """
        return int(len(self.vertices)) * 8


class Parse:
    """This class will parse a unity defined and compressed mesh if fed by string."""

    @staticmethod
    def parse_data_better(mesh: str) -> list:
        slices = []
        for offset in range(int(len(mesh) / 8)):
            offset = offset * 8
            # after much testing this is certainly little endian
            slices.append(unpack("<f", bytes.fromhex(mesh[offset : (offset + 8)]))[0])
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
            indices.append(unpack("<H", bytes.fromhex(index[offset : offset + 4]))[0])
        return indices

    @staticmethod
    def parse_mesh(m_IndexBuffer: str, _typelessdata: str):
        indices = Parse.parseIndicies(m_IndexBuffer)
        slices = Parse.parse_data_better(_typelessdata)
        vertices, normals = Parse.parse_intoMesh(slices)
        return indices, vertices, normals
