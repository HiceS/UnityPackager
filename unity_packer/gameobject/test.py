from gameobject import GameObject
from features.mesh import Mesh

def main():
    print("Tester for Gameobject")
    gameobj = GameObject("gameobject1")
    mesh = Mesh("asd", [], [], [])
    gameobj + mesh
    print(gameobj.features)

if __name__ == "__main__":
    main()