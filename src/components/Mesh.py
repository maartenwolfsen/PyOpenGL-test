from src.mesh.primitives.Cube import Cube
from src.mesh.primitives.Plane import Plane


class Mesh:
    def __init__(self, shape="cube", obj_path=False):
        self.shape = False

        if shape == "cube":
            self.shape = Cube()
        elif shape == "plane":
            self.shape = Plane()
        elif shape == "custom":
            # TODO custom shape
            if not obj_path:
                raise Exception("No Object Path was given for custom Mesh")

            self.shape = False

    def draw(self, transform):
        if not self.shape:
            raise Exception("Mesh Shape not set")

        self.shape.draw(transform)
