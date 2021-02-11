# loosely defined to fit basic material coloring

from unity_packer.gameobject.base import BaseUnity
from unity_packer.yaml.writer import GenerateYamlData
from unity_packer.yaml.format import (
    meshyaml,
    meshFilterYaml,
    meshRendererYaml,
    matBasicYaml,
    urp_mat
)

from enum import Enum

class MatType (Enum):
    STANDARD = 0
    URP = 1
    HDRP = 2

class Material:
    """This is a class used to define the material being used to create the mesh"""

    def __init__(
        self, name: str, mesh=None, r=1, g=1, b=1, a=1, smoothness=0.5, metallic=0.5, matType=MatType.STANDARD, GUID=None
    ):
        """Constructs a new materials

        Args:
            name (str): name of materials
            mesh (Mesh, optional): to directly link a mesh to a specific material, will automatically link all
            r (int, optional): red channel 0-1. Defaults to 1.
            g (int, optional): green channel 0-1. Defaults to 1.
            b (int, optional): blue channel 0-1. Defaults to 1.
            a (int, optional): alpha channel 0-1. Defaults to 1.
            smoothness (float, optional): smoothness value 0-1. Defaults to 0.5.
            metallic (float, optional): metallic value 0-1. Defaults to 0.5.
        """
        self.base = BaseUnity(name, GUID)

        self.r = r
        self.g = g
        self.b = b
        self.a = a
        self.smoothness = smoothness
        self.metallic = metallic
        self.matType = matType

    def serialize(self) -> str:

        material_data = {
            "ref_id": self.base.uuid_signed(),
            "name": self.base.name,
            "smoothness": self.smoothness,
            "metallic": self.metallic,
            "albedo_r": self.r,
            "albedo_g": self.g,
            "albedo_b": self.b,
            "albedo_a": self.a,
        }

        if (self.matType == MatType.STANDARD):
            return GenerateYamlData(material_data, matBasicYaml)
        
        if (self.matType == MatType.URP):
            return GenerateYamlData(material_data, urp_mat) 
