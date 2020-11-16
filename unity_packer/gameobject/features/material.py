from unity_packer.gameobject.base import BaseUnity
from unity_packer.yaml.format import meshRendererYaml
from unity_packer.yaml.writer import GenerateYamlData

class Material:
    def __init__(self, name: str):
        self.base = BaseUnity(name)
        self.materialBase = BaseUnity(f'{name}_material')

    def serialize(self)-> str:
        data = {
            "ref_id": self.base.uuid_signed(),
            'gameobject_fileID': self.base.gameobject.base.fileReference(),
        }

        return GenerateYamlData(data, meshRendererYaml)