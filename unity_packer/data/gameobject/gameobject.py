""" 
Object that is the equivalent of a unity gameobject,

Has a name and list of serializable objects.
"""

from .base import BaseUnity

class GameObject:
    def __init__(self, name: str):
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

