from src.primitives.Cube import Cube
from src.primitives.Plane import Plane
from src.GameObject import GameObject
from src.math.Vector3 import Vector3
from src.components.Transform import Transform
from src.components.Collider import Collider

class Scene:
    def __init__(self, name):
        self.name = name
        t1 = Transform(
            Vector3(0, -1, 0),
            Vector3(1, 1, 1),
            Vector3(100, 1, 100)
        )
        t2 = Transform(
            Vector3(1, 0, 4),
            Vector3(2, 2, 2),
            Vector3(2, 2, 2)
        )
        t3 = Transform(
            Vector3(-5, 0, 4),
            Vector3(2, 2, 2),
            Vector3(2, 2, 2)
        )
        t4 = Transform(
            Vector3(-8, -0.5, 4),
            Vector3(2, 2, 2),
            Vector3(2, 1, 2)
        )
        t5 = Transform(
            Vector3(4, 0, 4),
            Vector3(0, 0, 0),
            Vector3(0.5, 2, 0.5)
        )
        self.game_objects = [
            GameObject(
                "ground",
                t1,
                Plane(),
                Collider(t1)
            ),
            GameObject(
                "cube1",
                t2,
                Cube(),
                Collider(t2)
            ),
            GameObject(
                "cube2",
                t3,
                Cube(),
                Collider(t3)
            ),
            GameObject(
                "cube3",
                t4,
                Cube(),
                Collider(t4)
            ),
            GameObject(
                "enemy1",
                t5,
                Cube(),
                Collider(t5)
            ),
        ]

    def add(self, game_object):
        self.game_objects.append(game_object)
