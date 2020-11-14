""" Mesh Module that defines a mesh structure.

Mesh structure will be a factory that can utilize
the index buffer and typed data unity needs as part of the
rendering environment.

"""
from ..unityobject import UnityObject

class Mesh(UnityObject):
    self.vertices: list[float] = []
    """ List of all Vertices in Mesh

    format:
        - [{x}, {y}, {z}, {x}, {y}, {z}]
    """

    self.indices: list[int] = []
    """ List of all indices to connect vertices

    Must be 1/3 the size of the verticies list

    format:
        - [{triangle_1_x}, {triangle_2_y}, {triangle_3_z}]
    """

    self.normals: list[float] = []
    """ List of all normals for each vertices

        - Optional
    """
    
    self.uvs: list[int] = []
    """ List of all UVS in the current mesh

    Not currently supported
    """

    def __init__(self, name):
        super().__init__(name)

    def generateBuffer(self):
        pass

    def generateReference(self):
        """ Generates a reference to the mesh with a different transform
        """
        pass

