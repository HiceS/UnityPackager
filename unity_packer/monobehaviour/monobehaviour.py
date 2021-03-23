# Needs to create a new folder with a given ID
# Then needs to specify a path
# Then needs to specify the file itself
# Then needs to specify the public data available
from uuid import uuid4, UUID
from unity_packer.yaml.writer import GenerateYamlData
from unity_packer.yaml.format import monobehaviour_asset_meta, scriptpath
from unity_packer.gameobject.base import BaseUnity

from unity_packer.fileUtils import (
    generateAssetMetaFile,
    generatePathnameFile,
    createFolders,
)

import os, tarfile, shutil


class MonoBehaviour:
    """After creating a monobehaviour you can reference it as many times as you want"""

    def __init__(self, name: str, fullScriptLocation: str, GUID=None):
        self.base = BaseUnity(name, GUID)
        self.path = path
        self.fullScriptLocation = fullScriptLocation

    def serialize(self, outputPath, unity_tar) -> None:
        # Must create folders
        # Must add script to asset file
        # Must have some way to reference the script possibly

        # 1. Create a new GUID folder name
        # 2. Create sub folders
        # 3.

        # creates end directory if doesn't exist
        outdir = os.path.dirname(outputPath)

        if not os.path.exists(outdir):
            os.makedirs(outdir)

        tempdir = os.path.join(outdir, f"temp_{self.base.uuid_hex()}")

        if not os.path.exists(tempdir):
            os.makedirs(tempdir)

        assetFileLoc, pathnameLoc, assetMetaLoc = createFolders(self.base, tempdir)

        # create asset directory files
        generateAssetMetaFile(self.base, assetMetaLoc, monobehaviour_asset_meta)
        generatePathnameFile(self.base, pathnameLoc, scriptpath)

        # probably should do some check here
        shutil.copyfile(self.fullScriptLocation, assetFileLoc)

        # now create a tarfile
        with tarfile.open(unity_tar, mode="w") as archive:
            archive.add(assetFileLoc, arcname=f"{self.base.uuid_hex()}/asset")
            archive.add(pathnameLoc, arcname=f"{self.base.uuid_hex()}/pathname")
            archive.add(assetMetaLoc, arcname=f"{self.base.uuid_hex()}/asset.meta")

        # this is a dangerous game
        shutil.rmtree(tempdir)
