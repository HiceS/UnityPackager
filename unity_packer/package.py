"""
Defines a structure for exporting a unity package.

Structures defined will attempt to be packaged into a single file.

All listed classes added to the package structure will call a serialize method to create a yaml structure.

Will return a bytebuffer to represent the file that should be written ? Possibly just write the file or ask for a fileloc


Steps:

    1. Generate a Package Object
    2. Generate a Gameobject Object
    3. Generate a Mesh Object
    4. Add Mesh Object to Gameobject
    5. Add Gameobject to Package
    6. Write Gameobject

"""

from typing import List
import os
import tarfile
from pathlib import Path

import gzip
import shutil

from unity_packer.gameobject.gameobject import GameObject
from unity_packer.gameobject.mesh import Mesh
from unity_packer.gameobject.material import Material
from unity_packer.gameobject.base import BaseUnity
from unity_packer.yaml.format import assetmeta, pathname, assetTag
from unity_packer.yaml.writer import GenerateYamlData


class Package:
    def __init__(self, name: str):
        super().__init__()

        # name of the package and uuid for linking
        self.base = BaseUnity(name)

        # list of gameobject children
        self.children: List[GameObject] = []

        # list of meshes in package
        self.meshes: List[Mesh] = []

        # list of materials in package
        self.materials: List[Materials] = []

    ### __Section dedicated to internal functions for writing data__ ##

    def __generateAssetMetaFile(self, loc: str):
        """Generates the Asset.meta file in the uuid directory

        - asset.meta
        """
        data = {
            "ref_id": self.base.uuid_hex(),
        }
        assetfile = GenerateYamlData(data, assetmeta)

        with open(loc, "r+") as f:
            f.write(assetfile)

    def __generatePathnameFile(self, loc: str):
        """Generates the pathname file in the uuid directory

        - pathname
        """
        data = {"name": self.base.name}
        pathnamefile = GenerateYamlData(data, pathname)

        with open(loc, "r+") as f:
            f.write(pathnamefile)

    def __createFolder(self, outpath):

        # just in case
        if not os.path.exists(outpath):
            os.makedirs(outpath)

        # ./output

        uuidDirectory = os.path.join(outpath, self.base.uuid_hex())
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

    def addMesh(self, mesh: Mesh):
        self.meshes.append(mesh)

    def addMaterial(self, material: Material):
        self.materials.append(material)

    def serialize(self, outpathfull, tempdir) -> str:
        """ Serializes the data of all the children

        Args:
            outpathfull (Path): path of the unitypackage to be constructed
            tempdir (Path): teomporary storage location for buffer writing

        Returns:
            str: returns path and file name
        """
        outdir = os.path.dirname(outpathfull)

        if not os.path.exists(outdir):
            os.makedirs(outdir)

        # make this a real temp dir
        tempdir = os.path.join(outdir, f"temp_{self.base.uuid_hex()}")

        if not os.path.exists(tempdir):
            os.makedirs(tempdir)

        assetFileLoc, pathnameLoc, assetMetaLoc = self.__createFolder(tempdir)

        # create asset directory files
        self.__generateAssetMetaFile(assetMetaLoc)
        self.__generatePathnameFile(pathnameLoc)

        # write all the meshes and materials first
        with open(assetFileLoc, "a+") as f:
            f.write(assetTag)

            for material in self.materials:
                f.write(material.serialize())

            for mesh in self.meshes:
                f.write(mesh.serialize())

        # generate gameobjects
        # foreach child add the serialized objects to file
        for child in self.children:
            # im assuming that you only stored gameobjects in here
            # append will check
            child.serialize(assetFileLoc)

        archtemp = "archtemp.tar"

        unity_tar = os.path.join(tempdir, archtemp)

        # now create a tarfile
        with tarfile.open(unity_tar, mode="w") as archive:
            archive.add(assetFileLoc, arcname=f"{self.base.uuid_hex()}/asset")
            archive.add(pathnameLoc, arcname=f"{self.base.uuid_hex()}/pathname")
            archive.add(assetMetaLoc, arcname=f"{self.base.uuid_hex()}/asset.meta")

        with open(unity_tar, "rb") as f_in:
            with open(outpathfull, "wb") as f_out:
                with gzip.GzipFile(unity_tar, fileobj=f_out) as f:
                    shutil.copyfileobj(f_in, f)

        shutil.rmtree(tempdir)

        return outpathfull

    #### __Section for Adding Gameobjects___ ####

    def __add__(self, gameobject):
        """Overriding the plus operator to add a gameobject

        Args:
            gameobject (List[GameObject]): returns the updated list of gameobjects

        Returns:
            This class for multiple overrides (this + gameobject) + gameobject
        """
        self.addGameobject(gameobject)
        return self

    def addGameobject(self, gameobject: GameObject) -> None:
        """Adds a gameobject to children to be serialized

        Args:
            gameobject (GameObject): gameobject to be added

        Raises:
            TypeError: If gameobject is not of type Gameobject
        """
        if type(gameobject) is GameObject:
            gameobject.packageID = self.base.uuid_hex()
            self.children.append(gameobject)
        else:
            raise TypeError("Supplied argument is not of type GameObject")

    def append(self, gameobject) -> None:
        self.addGameobject(gameobject)
