""" 
Object that is the equivalent of a unity gameobject,

Has a name and list of serializable objects.
"""
from __future__ import annotations

from unity_packer.yaml.format import gameobjectYaml
from unity_packer.yaml.writer import GenerateYamlData

from unity_packer.gameobject.base import BaseUnity
from unity_packer.gameobject.transform import Transform, Vector3

from typing import Union


class GameObject:
    def __init__(self, name: str, parent=None):
        super().__init__()

        # generates a name and guid for linking
        self.base = BaseUnity(name)

        self.features = []
        """ Features is a list of all gameobject features

         - Mesh
         - Materials
         - Joints
         - Etc.
        """

        # parent is the parent gameobject or none if at top level
        self.parent = parent
        """ Parents is the parent gameobject

            - None if parent gameobject for assembly
        """

        self.packageID = ""

        if parent:
            self.transform = Transform(self, parent=parent.transform)
        else:
            self.transform = Transform(self)

    ## These are different because local position may be modified by scale?
    ## Also in case there are infact differences later

    def setLocalPosition(self, vec: Vector3):
        """Sets the local position relative to the parent transform of the current gameobject

        Args:
            vec (Vector3): New position
        """
        self.transform.setLocal(vec)

    def setWorldPosition(self, vec: Vector3):
        """Sets the World Transform Position

        Args:
            vec (Vector3): New position
        """
        self.transform.setWorld(vec)

    def addChild(self, child: Union(GameObject | Transform)):
        """Adds a child to the current gameobject that is reflected in the Transform

        Args:
            child (Gameobject | Transform): child object to be referenced

        Raises:
            TypeError: Not a Gameobject or Transform Object
        """
        if type(child) == GameObject:
            self.transform.addChild(child.transform)
        elif type(child) == Transform:
            self.transform.addChild(child)
        else:
            raise TypeError(
                f"Child object being added to Gameobject {self.base.name} is not of type Gameobject or Transform"
            )

    def setParent(self, parent: Union(GameObject | Transform)):
        """Adds a parent to the current gameobject that is reflected in the Transform

        Args:
            parent (Gameobject | Transform): parent object to be referenced

        Raises:
            TypeError: Not a Gameobject or Transform Object
        """
        if type(parent) == GameObject:
            self.transform.setParent(parent.transform)
        elif type(parent) == Transform:
            self.transform.setParent(parent)
        else:
            raise TypeError(
                f"Parent object being added to Gameobject {self.base.name} is not of type Gameobject or Transform"
            )

    def serialize(self, loc):
        components = ""

        with open(loc, "a+") as f:
            # create the transform that will link the object
            f.write(self.transform.serialize())
            components = (
                f"{components}\n  - component: {self.transform.base.fileReference()}"
            )

            # this will add all serialized objects and we need to keep list of components
            for feature in self.features:
                f.write(feature.serialize())
                # this is really only for transform? and other monobehaviours - lets just make mesh a meshrenderer
                components = (
                    f"{components}\n  - component: {feature.base.fileReference()}"
                )

            data = {
                "ref_id": self.base.uuid_signed(),
                "components": components,
                "name": self.base.name,
            }

            f.write(GenerateYamlData(data, gameobjectYaml))

    def __str__(self):
        return self.base.fileReference()

    #### __Section for Adding Features__ ####

    def __add__(self, feature):
        """Overriding the plus operator to add a feature

        Args:
            gameobject (List[feature]): returns the updated list of features

        Returns:
            This class for multiple overrides (this + feature) + feature
        """
        self.addFeature(feature)
        return self

    def addFeature(self, feature: any) -> None:
        """Adds a gameobject to children to be serialized

        Args:
            gameobject (GameObject): gameobject to be added

        Raises:
            TypeError: If gameobject is not of type Gameobject
        """
        feature.base.gameobject = self
        self.features.append(feature)

    def updateFeatures(self) -> None:
        """To be called by the copy reference to update the feature references to the newest gameobject id"""
        for feature in self.features:
            feature.base.gameobject = self

    def append(self, feature) -> None:
        self.addFeature(feature)

    @classmethod
    def CopyReferences(cls, gameobject: GameObject) -> GameObject:
        """Copies the references from another gameobject

        Args:
            gameobject (GameObject): Gameobject to copy

        Returns:
            GameObject: newly created gameobject
        """
        new_gameobject = cls(gameobject.base.name, gameobject.parent)
        new_gameobject.transform = Transform.CopyReferences(
            new_gameobject, gameobject.transform
        )
        new_gameobject.features = gameobject.features.copy()
        new_gameobject.updateFeatures()
        return new_gameobject
