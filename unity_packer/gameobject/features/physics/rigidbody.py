from unity_packer.gameobject.base import BaseUnity
from unity_packer.yaml.writer import GenerateYamlData
from unity_packer.yaml.format import rigidBodyYaml


class Rigidbody:
    def __init__(self, name="rigidbody"):
        self.base = BaseUnity(name)
        self.mass = 0.0

    def serialize(self):

        collider_data = {
            "ref_id": self.base.uuid_signed(),
            "gameobject_fileID": self.base.gameobject.base.fileReference(),
            "mass": f"{self.mass}",
        }

        return GenerateYamlData(collider_data, rigidBodyYaml)
