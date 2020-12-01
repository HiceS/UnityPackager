from __future__ import annotations
from typing import List, Union

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

        # this is theoretically the parent transform
        self.parent = parent

        # list of all child transforms fileIDs - children need to be a fileID type
        self.children = []

        self.gameobject = gameobject
        """ Parent transform
        """

    def addChild(self, child: Transform):
        """Adds child to transform

        Args:
            child (Transform): child object to add reference

        Raises:
            TypeError: child is not a Transform
        """
        if type(child) == Transform:
            self.children.append(child.base.fileReference())
        else:
            raise TypeError(
                f"Attempted to add child to Transform {self.base.name} that is not of type Transform"
            )

    def setParent(self, parent: Transform):
        """Assigns a new parent to the transform

        Args:
            parent (Transform): parent object in hierarchy

        Raises:
            TypeError: parent is not a Transform
        """
        if type(parent) == Transform:
            self.parent = parent.base.uuid_signed()
        else:
            raise TypeError(
                f"Supplied parent to setParent of transform {self.base.name} is not of type Transform"
            )

    def serialize(self):
        if self.parent is None:
            self.parent = ""

        children_str = ""

        # compound a list of children to link against
        for child in self.children:
            children_str = f"{children_str}\n  - {child}"

        vec_1 = str(Vector3.One())

        data = {
            "ref_id": self.base.uuid_signed(),
            "gameobject": self.gameobject,
            "position_vec3": str(self.local),
            "scale_vec3": vec_1,
            "children": children_str,
            "parent": self.parent,
            "rotation_quat": vec_1,
            "eulerangle_vec3": vec_1,
        }

        return GenerateYamlData(data, transformYaml)

    def setLocal(self, vec):
        self.local = vec

    def setWorld(self, vec):
        self.world = vec

    @classmethod
    def CopyReferences(cls, gameobject: Gameobject, transform: Transform) -> Transform:
        new_transform = cls(
            gameobject,
            parent=transform.parent,
            local=transform.local,
            world=transform.world,
        )
        new_transform.children = transform.children.copy()
        return new_transform


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
