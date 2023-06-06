from src.Vector3 import Vector3
from src.components.Transform import Transform


class Player:
    def __init__(self):
        self.transform = Transform(
            Vector3(0, 0, 0),
            Vector3(0, 0, 0),
            Vector3(1, 1, 1)
        )

        self.speed = 0.05
