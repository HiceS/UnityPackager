class UnityObject:
    """ Base class for many of the unity types
    """
    name = ""
    
    def __init__(self, name = ""):
        self.name = name