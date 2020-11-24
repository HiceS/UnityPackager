#!/usr/bin/env python3
"""
This module tests the ability to parse and create meshes

Parses the cubed indexbuffer that is currently in hex form

usage:
    ` python test.py `
"""
from unity_packer.gameobject.mesh import Mesh, Parse
from unity_packer.gameobject.material import Material
from unity_packer.gameobject.features.filter import Filter
from unity_packer.gameobject.features.renderer import Renderer
from unity_packer.package import Package
from unity_packer.gameobject.gameobject import GameObject

import os, shutil


# field `_typelessdata`
mesh = "cdcc4c3dcdcc4c3d000000000000000000000000000080bf00000000cdcc4c3d000000000000000000000000000080bf0000000000000000000000000000000000000000000080bfcdcc4c3d00000000000000000000000000000000000080bf00000000cdcc4c3dcdcc4c3d00000000000000000000803fcdcc4c3dcdcc4c3dcdcc4c3d00000000000000000000803fcdcc4c3d00000000cdcc4c3d00000000000000000000803f0000000000000000cdcc4c3d00000000000000000000803f00000000cdcc4c3d00000000000000000000803f00000000cdcc4c3dcdcc4c3d00000000000000000000803f00000000cdcc4c3dcdcc4c3dcdcc4c3d000000000000803f0000000000000000cdcc4c3dcdcc4c3d000000000000803f00000000cdcc4c3dcdcc4c3d000000000000803f0000000000000000cdcc4c3d00000000000000000000803f0000000000000000cdcc4c3d00000000cdcc4c3d0000803f0000000000000000cdcc4c3dcdcc4c3dcdcc4c3d0000803f0000000000000000cdcc4c3d000000000000000000000000000080bf0000000000000000000000000000000000000000000080bf000000000000000000000000cdcc4c3d00000000000080bf00000000cdcc4c3d00000000cdcc4c3d00000000000080bf00000000000000000000000000000000000080bf000000000000000000000000cdcc4c3d00000000000080bf000000000000000000000000cdcc4c3dcdcc4c3d000080bf00000000000000000000000000000000cdcc4c3d000080bf0000000000000000"

# field "`m_IndexBuffer`
index = "1600150017001700150014001200110013001300110010000e000d000f000f000d000c000a0009000b000b0009000800060005000700070005000400020001000300030001000000"


def main():
    dir_out = os.path.join(os.getcwd(), "output")

    try:
        shutil.rmtree(dir_out)
    except OSError as e:
        print("Error: %s : %s" % (dir_out, e.strerror))

    indices, vertices, normals = parseIndexBuffer()
    constructIndexBufferNew(indices, vertices, normals)


def constructIndexBufferNew(indices, vertices, normals):
    print(f"\nTriangles from indices size : {len(indices) / 3}")
    print(f"vertices size: {len(vertices) / 3}")
    print(f"normals size: {len(normals) / 3}\n")

    _mesh = Mesh("cube_tester", vertices, indices, normals)

    print(f"Vertices (parsed):\n{vertices}\n")
    print(f"Indices (parsed):\n{indices}\n")
    print(f"Normals (parsed):\n{normals}\n")

    # print("Previous UnTyped Buffer vs. Generated:\n")
    # print(_mesh._generateUntypedBuffer())
    # print("\n" + mesh + "\n\n")

    # print("Previous Index Buffer vs. Generated:\n")
    # print(_mesh._generateIndexBuffer())
    # print("\n" + index)

    package = Package("tester")
    rootgameobject = GameObject("RootGameObject")

    renderer = Renderer()
    _filter = Filter()

    material = Material("steel-satin", 0.2, 1.0, 0.5, 1.0, 0.5, 1.0)
    renderer.addMaterial(material)

    _filter.append(_mesh.getReference())

    package.addMesh(_mesh)
    package.addMaterial(material)

    rootgameobject.append(_filter)
    rootgameobject.append(renderer)

    package.append(rootgameobject)
    # package._generateAssetFile()
    # package._generatePathnameFile()
    out = os.path.join(os.getcwd(), "Test.unitypackage")
    package.serialize(out)


def parseIndexBuffer():
    return Parse.parse_mesh(index, mesh)


if __name__ == "__main__":
    main()
