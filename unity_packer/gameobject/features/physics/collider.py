from unity_packer.gameobject.base import BaseUnity
from unity_packer.yaml.writer import GenerateYamlData
from unity_packer.yaml.format import (
    meshCollider
)

class Collider:
    def __init__(self, name="collider"):
        self.base = BaseUnity(name)
        self.mesh_ref = None

    def serialize(self):

        collider_data = {
            "ref_id": self.base.uuid_signed(),
            "gameobject_fileID": self.base.gameobject.base.fileReference(),
            "mesh_ref_fileID": f"{BaseUnity.uuidToFileRef(self.mesh_ref)}",
        }

        return GenerateYamlData(collider_data, meshCollider)