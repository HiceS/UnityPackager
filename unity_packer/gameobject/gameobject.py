""" 
Object that is the equivalent of a unity gameobject,

Has a name and list of serializable objects.
"""

from unity_packer.gameobject.base import BaseUnity
from unity_packer.gameobject.transform import Transform, Vector3

class GameObject:
    def __init__(self, name: str):
        super().__init__()

        # generates a name and guid for linking
        self.base = BaseUnity(name)

        self.transform = Transform()

        self.features = []
        """ Features is a list of all gameobject features

         - Mesh
         - Materials
         - Joints
         - Etc.
        """

    ## These are different because local position may be modified by scale?
    ## Also in case there are infact differences later

    def setLocalPosition(self, vec):
        self.transform.setLocal(vec)

    def setWorldPosition(self, vec):
        self.transform.setWorld(vec)

    #### __Section for Adding Features___#### 

    def __add__(self, feature):
        """ Overriding the plus operator to add a feature

        Args:
            gameobject (List[feature]): returns the updated list of features

        Returns:
            This class for multiple overrides (this + feature) + feature
        """
        self.addFeature(feature)
        return self

    def addFeature(self, feature: any) -> None:
        """ Adds a gameobject to children to be serialized

        Args:
            gameobject (GameObject): gameobject to be added

        Raises:
            TypeError: If gameobject is not of type Gameobject
        """
        self.features.append(feature)

    def append(self, feature) -> None:
        self.addFeature(feature)

