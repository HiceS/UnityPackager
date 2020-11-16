""" 
Object that is the equivalent of a unity gameobject,

Has a name and list of serializable objects.
"""
from unity_packer.yaml.format import gameobjectYaml
from unity_packer.yaml.writer import GenerateYamlData

from unity_packer.gameobject.base import BaseUnity
from unity_packer.gameobject.transform import Transform, Vector3

class GameObject:
    def __init__(self, name: str, parent = None):
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

        # child gameobjects
        self.children = []
        """ Children is a list of child gameobjects on the first level
        """

        # parent is the parent gameobject or none if at top level
        self.parent = parent
        """ Parents is the parent gameobject

            - None if parent gameobject for assembly
        """

        if (parent):
            self.transform = Transform(self, parent=parent.transform)
        else:
            self.transform = Transform(self)

    ## These are different because local position may be modified by scale?
    ## Also in case there are infact differences later

    def setLocalPosition(self, vec):
        self.transform.setLocal(vec)

    def setWorldPosition(self, vec):
        self.transform.setWorld(vec)

    def serialize(self, loc):
        components = ""

        with open(loc, "a+") as f:
            # create the transform that will link the object 
            f.write(self.transform.serialize())
            components = f'{components}\n  - component: {self.transform.base.fileReference()}'

            # this will add all serialized objects and we need to keep list of components
            for feature in self.features:
                f.write(feature.serialize(self))

                # this is really only for transform? and other monobehaviours - lets just make mesh a meshrenderer
                components = f'{components}\n  - component: {feature.base.fileReference()}'

            data = {
                "ref_id" : self.base.uuid,
                "components" : components,
                "name": self.base.name
            }

            f.write(GenerateYamlData(data, gameobjectYaml))

    def __str__(self):
        return self.base.fileReference()


    #### __Section for Adding Features__ #### 

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

