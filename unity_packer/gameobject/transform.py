from typing import List

class Transform():
    """ Class for defining simple 3D space transforms
    """
    def __init__(self, local = None, world = None):
        if (local):
            self.local = local
        else:
            self.position = Vector3.Zero()

        if (world):
            self.world = world
        else:
            self.world = Vector3.Zero()

    def setLocal(self, vec):
        self.local = vec

    def setWorld(self, vec):
        self.world = vec


class Vector3():
    """ Storing a 3D or 2D position

    Members:
        - X (float)
        - Y (float)
        - Z (float)
    """
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0

    def __init__(self, x = 0.0, y = 0.0, z = 0.0):
        self.x = x
        self.y = y
        self.z = z
        
    @classmethod
    def Zero(cls):
        """ Returns a zero position vector
        """
        return cls(float(0.0), float(0.0), float(0.0))