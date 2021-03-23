from unity_packer.yaml.writer import GenerateYamlData
from unity_packer.gameobject.base import BaseUnity
import os, shutil


def generateAssetMetaFile(baseObject, loc: str, yamlFormat: str):
    """Generates the Asset.meta file in the uuid directory

    - asset.meta
    """
    data = {
        "ref_id": baseObject.uuid_hex(),
    }
    assetfile = GenerateYamlData(data, yamlFormat)

    with open(loc, "r+") as f:
        f.write(assetfile)


def generatePathnameFile(baseObject, loc: str, yamlFormat: str):
    """Generates the pathname file in the uuid directory

    - pathname
    """
    data = {"name": baseObject.name}
    pathnamefile = GenerateYamlData(data, yamlFormat)

    with open(loc, "r+") as f:
        f.write(pathnamefile)


def createFolders(baseObject, outpath):

    # just in case
    if not os.path.exists(outpath):
        os.makedirs(outpath)

    # ./output
    uuidDirectory = os.path.join(outpath, baseObject.uuid_hex())
    if not os.path.exists(uuidDirectory):
        os.makedirs(uuidDirectory)

    # ./output/uuid
    assetFile = os.path.join(uuidDirectory, "asset")
    with open(assetFile, "w") as f:
        pass

    pathnameFile = os.path.join(uuidDirectory, "pathname")
    with open(pathnameFile, "w") as f:
        pass

    assetMetaFile = os.path.join(uuidDirectory, "asset.meta")
    with open(assetMetaFile, "w") as f:
        pass

    return assetFile, pathnameFile, assetMetaFile
