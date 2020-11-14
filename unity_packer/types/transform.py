class Transform():
    self.name = ""
    self.position = Position.Zero()

    def __init__(self, name: str, position = None):
        self.name = name
        if (position):
            self.position = position


class Position():
    """ Storing a 3D or 2D position

    Members:
        - X (float)
        - Y (float)
        - Z (float)
    """
    self.x: float = 0.0
    self.y: float = 0.0
    self.z: float = 0.0

    def __init__(self, x = 0.0, y = 0.0, z = 0.0):
        self.x = x
        self.y = y
        self.z = z

    def __init__(self, listed: list[float]):
        if (len(listed) > 0):
            self.x = listed[0] if listed[0] else 0
            self.y = listed[1] if listed[1] else 0
            self.z = listed[2] if listed[2] else 0

    @classmethod
    def Zero(cls):
        """ Returns a zero position vector
        """
        return cls(0.0, 0.0, 0.0)