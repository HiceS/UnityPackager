""" Mesh Module that defines a mesh structure.

Mesh structure will be a factory that can utilize
the index buffer and typed data unity needs as part of the
rendering environment.

"""
from ..unityobject import UnityObject

from ctypes import c_float, c_uint16

from typing import List
from struct import pack, unpack

class Mesh(UnityObject):


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

        ret = "";

        # a good note is that len(verticies) === len(normals)

        # python regular float is interpreted as double precision as far as I understand
        # convert each value in vertices to f32 from generic float
        #   - c_float is 4 bytes which is what we need to eliminate extra precision

        # this should pack the data for each point into a 32 bit float
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

    def generateReference(self) -> str:
        """ Generates a YAML reference

        Returns:
            str: yaml reference to the mesh
        """
        return ""

import math

def hex2float(num):
    sign = (num & 0x80000000) if -1 else 1
    exponent = ((num >> 23) & 0xff) - 127
    mantissa = 1 + ((num & 0x7fffff) / 0x7fffff)
    return sign * mantissa * math.pow(2, exponent)

def swap16(val):
    return ((val & 0xFF) << 8) | ((val >> 8) & 0xFF)

def swap32(val):
    return (
    ((val << 24) & 0xff000000) |
    ((val << 8) & 0xff0000) |
    ((val >> 8) & 0xff00) |
    ((val >> 24) & 0xff)
    )

class Parse():
    @staticmethod
    def parse_data_better(mesh: str) -> list:
        slices = []
        for offset in range(int(len(mesh) / 8)):
            offset = offset * 8
            # after much testing this is certainly little endian
            slices.append(unpack('<f', bytes.fromhex(mesh[offset : (offset + 8)]))[0])
        return slices

    @staticmethod
    def parse_typeless(mesh: str) -> list:
        slices = []
        for offset in range(int(len(mesh) / 8)):
            offset = (offset * 8)
            hexnum = int(mesh[offset : (offset + 8)], 16)
            slicer = hex2float(swap32(hexnum))
            slices.append(slicer)
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
            indexInt = int(index[offset: offset + 4], 16)
            indices.append(swap16(indexInt));
        return indices

    @staticmethod
    def parse_mesh(m_IndexBuffer: str, _typelessdata: str):
        indices = Parse.parseIndicies(m_IndexBuffer)
        slices = Parse.parse_data_better(_typelessdata)
        vertices, normals = Parse.parse_intoMesh(slices)

        print(f"Traingles from indices size : {len(indices) / 3}")
        print(f"vertices size: {len(vertices) / 3}")
        print(f"normals size: {len(normals) / 3}")
        print(f"slices size: {len(slices)}")

        return indices, vertices, normals