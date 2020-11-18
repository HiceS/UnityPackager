from typing import List

from unity_packer.gameobject.base import BaseUnity
from unity_packer.yaml.format import transformYaml
from unity_packer.yaml.writer import GenerateYamlData


class Transform:
    """Class for defining simple 3D space transforms"""

    def __init__(self, gameobject, parent=None, local=None, world=None):
        if parent:
            self.base = BaseUnity(f"{gameobject.name}_transform")
        else:
            self.base = BaseUnity("root_transform")

        if local:
            self.local = local
        else:
            self.local = Vector3.Zero()

        if world:
            self.world = world
        else:
            self.world = Vector3.Zero()

        self.parent = parent
        self.gameobject = gameobject
        """ Parent transform
        """

    def serialize(self):
        if self.parent is None:
            self.parent = ""

        vec_1 = str(Vector3.One())

        data = {
            "ref_id": self.base.uuid_signed(),
            "gameobject": self.gameobject,
            "position_vec3": str(self.local),
            "scale_vec3": vec_1,
            "children": "",
            "parent": self.parent,
            "rotation_quat": vec_1,
            "eulerangle_vec3": vec_1,
        }

        return GenerateYamlData(data, transformYaml)

    def setLocal(self, vec):
        self.local = vec

    def setWorld(self, vec):
        self.world = vec


class Vector3:
    """Storing a 3D or 2D position

    Members:
        - X (float)
        - Y (float)
        - Z (float)
    """

    x: float = 0.0
    y: float = 0.0
    z: float = 0.0

    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"x: {self.x}, y: {self.y}, z: {self.z}"

    @classmethod
    def Zero(cls):
        """Returns a zero position vector"""
        return cls(float(0.0), float(0.0), float(0.0))

    @classmethod
    def One(cls):
        """Returns a zero position vector"""
        return cls(float(1.0), float(1.0), float(1.0))
