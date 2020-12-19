from unity_packer.gameobject.base import BaseUnity
from unity_packer.yaml.writer import GenerateYamlData
from unity_packer.yaml.format import (
    meshCollider
)


class Joint:
    def __init__(self, name="joint"):
        self.base = BaseUnity(name)

    def serialize(self):
        return ""