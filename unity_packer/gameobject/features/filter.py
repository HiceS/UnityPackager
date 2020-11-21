
from unity_packer.gameobject.base import BaseUnity
from unity_packer.gameobject.mesh import Mesh
from unity_packer.yaml.writer import GenerateYamlData
from unity_packer.yaml.format import (
    meshyaml,
    meshFilterYaml,
    meshRendererYaml,
    matBasicYaml,
)

class Filter:
    """This is a class used to define the filter to link the meshes to the gameobject
    
    - add a gameobject
    - add a filter
    - append a mesh to the filter which addes the mesh id
    """

    def __init__(self, name="filter"):
        self.base = BaseUnity(name)
        self.meshes = []

    def serialize(self):
        filter_data = {
            "ref_id": self.base.uuid_signed(),
            "gameobject_fileID": self.base.gameobject.base.fileReference(),
            "mesh_ref_fileID": f"{BaseUnity.uuidToFileRef(self.meshes[0])}",
        }

        return GenerateYamlData(filter_data, meshFilterYaml)

    def __add__(self, mesh: int):
        """Overriding the plus operator to add a Mesh

        Args:
            Mesh (List[Mesh]): returns the updated list of Mesh

        Returns:
            This class for multiple overrides (this + Mesh) + Mesh
        """
        self.addMesh(mesh)
        return self

    def addMesh(self, mesh: int) -> None:
        """Adds a Mesh to children to be serialized

        Args:
            Mesh (Mesh): Mesh to be added

        Raises:
            TypeError: If Mesh is not of type Mesh
        """
        # just save a formatted reference to the file?
        self.meshes.append(mesh)

    def append(self, mesh) -> None:
        self.addMesh(mesh)