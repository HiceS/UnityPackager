"""
Defines a structure for exporting a unity package.

Structures defined will attempt to be packaged into a single file.

All listed classes added to the package structure will call a serialize method to create a yaml structure.

Will return a bytebuffer to represent the file that should be written ? Possibly just write the file or ask for a fileloc


Steps:

    1. Generate a Package Object
    2. Generate a Gameobject Object
    3. Generate a Mesh Object
    4. Add Mesh Object to Gameobject
    5. Add Gameobject to Package
    6. Write Gameobject

"""

from typing import List

from .gameobject.gameobject import GameObject
from .gameobject.base import BaseUnity

class Package:
    def __init__(self, name: str):
        super().__init__()

        # name of the package and uuid for linking
        self.base = BaseUnity(name)

        # list of gameobject children
        self.children: List[GameObject] = []


    #### __Section for Adding Gameobjects___ #### 

    def __add__(self, gameobject):
        """ Overriding the plus operator to add a gameobject

        Args:
            gameobject (List[GameObject]): returns the updated list of gameobjects

        Returns:
            This class for multiple overrides (this + gameobject) + gameobject
        """
        self.addGameobject(gameobject)
        return self

    def addGameobject(self, gameobject: GameObject) -> None:
        """ Adds a gameobject to children to be serialized

        Args:
            gameobject (GameObject): gameobject to be added

        Raises:
            TypeError: If gameobject is not of type Gameobject
        """
        if (type(gameobject) is GameObject):
            self.children.append(gameobject)
        else:
            raise TypeError("Supplied argument is not of type GameObject")

    def append(self, gameobject) -> None:
        self.addGameobject(gameobject)
