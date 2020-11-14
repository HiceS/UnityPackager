#!/usr/bin/env python3

from data.spatial.mesh import Mesh, Parse
from test_data import index, mesh

def main():
    indices, vertices, normals = parseIndexBuffer()
    constructIndexBufferNew(indices, vertices, normals)

def constructIndexBufferNew(indicies, vertices, normals):
    _mesh = Mesh(
        "test",
        vertices,
        indicies,
        normals
    )

    print(vertices)
    print(indicies)
    print(normals)

    print(_mesh._generateUntypedBuffer())
    print("\n" + mesh + "\n\n")

    print(_mesh._generateIndexBuffer())
    print("\n" + index)

def constructIndexBuffer():
    mesh = Mesh(
        "test",
        [float(0.1245), float(0.1265), float(1.567343)],
        [0, 1, 2],
        [float(0.00), float(123.123), float(56.987676)]
        )
    print(mesh._generateUntypedBuffer())
    print(mesh._generateIndexBuffer())

def parseIndexBuffer():
    return Parse.parse_mesh(index, mesh)

if __name__ == "__main__":
    main()