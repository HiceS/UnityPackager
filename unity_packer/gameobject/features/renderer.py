# This class will be how you add a material to the mesh itself
# Not the greatest way to do things but circular dependencies are an issue

from unity_packer.gameobject.base import BaseUnity
from unity_packer.yaml.writer import GenerateYamlData
from unity_packer.yaml.format import (
    meshyaml,
    meshFilterYaml,
    meshRendererYaml,
    matBasicYaml,
)


class Renderer:
    """This is a class used to define the renderer being used to display the material on a gameobject"""

    def __init__(self, name="renderer"):
        """ Constructs a new meshrenderer """
        self.base = BaseUnity(name)

        self.materials = []
        """ List of materials that you may apply to the bodies
        """

    def addMaterialReference(self, mat_ref):
        self.materials.append(mat_ref)

    def addMaterial(self, material):
        self.materials.append(material.base.fileReference())

    def serialize(self) -> str:
        renderer_mats_attr = ""

        for material in self.materials:
            renderer_mats_attr = (
                f"{renderer_mats_attr}\n  - {material}"
            )

        # for renderer
        renderer_data = {
            "ref_id": self.base.uuid_signed(),
            "gameobject_fileID": self.base.gameobject.base.fileReference(),
            "materials": renderer_mats_attr,
        }

        mesh_renderer = GenerateYamlData(renderer_data, meshRendererYaml)

        return f"{mesh_renderer}"
