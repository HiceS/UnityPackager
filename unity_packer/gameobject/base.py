""" Simple way to create a base Data class for everything
"""
from uuid import uuid4, UUID
from struct import pack


class BaseUnity:
    """Base class for many of the unity types"""

    def __init__(self, name="", GUID=None):
        self.name = name

        # parent gameobject for a feature or none for gameobject itself
        self.gameobject = None

        # for saving GUID values
        self.uuid = GUID if (GUID != None and isinstance(GUID, UUID)) else uuid4()

        """ Unique ID that can be referenced in YAML

        TODO: investigate further if not linking

        I can't tell what the format is right away however,
        I just hope it will take a normal int as input and not try to dervice extraneous data from it.
        """

    def uuid_signed(self) -> str:
        """This is used internally in the asset file and needs to be 64bit signed

        Returns:
            str: string equivalent
        """
        # -8644223184479265925 (original)
        # 15766082941283354748 (shifted 64)
        # 2367906456961032846 (shifted 65)
        # 13657919909056279358 (shifted 64)
        # 2376124294814920691 (original)
        # 18446744073709551616

        # this isn't actually safe but oh well
        unsigned = self.uuid.int >> 65

        return str(unsigned)

    def uuid_hex(self) -> str:
        """This is used to link the folder that use hex

        Returns:
            str: hex uuid
        """
        return str(self.uuid.hex)

    def fileReference(self) -> str:
        """Generates a file reference for the guid

        Note:
            - This is not actually another file, unity calls it by that name
            - it can be but for now it won't be.

        Returns:
            str: the container of a file reference
        """
        return "{fileID: " + str(self.uuid_signed()) + "}"

    @staticmethod
    def uuidToFileRef(uuid):
        return "{fileID: " + str(uuid) + "}"
