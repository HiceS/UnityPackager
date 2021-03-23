# This is a script feature
# You still need to manually append the script unique ID as well as any additional data
# Every script needs a place to be saved as well as a reference number that is consistent
# This is just to attach the script, then I can have an additional field for all the other stuff

from unity_packer.gameobject.base import BaseUnity
from unity_packer.yaml.writer import GenerateYamlData
from unity_packer.yaml.format import c_sharp_script
from unity_packer.gameobject.gameobject import GameObject


class Script:
    def __init__(self, scriptID: str, name="script"):
        """This is the script reference section

        Args:
            scriptID (str): monobehaviour reference
            name (str, optional): script basic name. Defaults to "script".
        """
        self.base = BaseUnity(name)
        self.scriptID = scriptID
        self.params = dict()

    def addParam(self, param: str, value: any):
        """Add a parameter to the given script - referenced from inspector

        Args:
            param (str): parameter name exactly as displayed
            value (any): value of param - can give GameObject/Transform directly
        """
        # if this is a gameobject you need to specify the full file ref
        if type(value) == "GameObject":
            value = value.base.fileReference()
        # needs to check for array types
        self.params[param] = value

    def __paramsToYaml(self) -> str:
        paramsYaml = ""
        for param, value in self.params.items:
            paramsYaml += f"{param}: {value}\n"

    def serialize(self):

        script_data = {
            "ref_id": self.base.uuid_signed(),
            "gameobject_fileID": self.base.gameobject.base.fileReference(),
            "m_script": self.scriptID,
        }

        return f"{GenerateYamlData(script_data, c_sharp_script)}{self.__paramsToYaml()}"
