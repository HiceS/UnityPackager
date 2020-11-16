from uuid import uuid4

class UnityObject:
    """ Base class for many of the unity types
    """
    
    def __init__(self, name = ""):
        self.name = name
    
        self.uuid: int = uuid4().int
        """ Unique ID that can be referenced in YAML

        TODO: investigate further if not linking

        I can't tell what the format is right away however,
        I just hope it will take a normal int as input and not try to dervice extraneous data from it.
        """