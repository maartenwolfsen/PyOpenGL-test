from src.math.Vector3 import Vector3


class PhysicsBody:
    def __init__(self, drag):
        self.velocity = Vector3(0, 0, 0)
        self.drag = 0
        self.mass = 0

    def apply_force(self, force):
        self.velocity = self.velocity + force
