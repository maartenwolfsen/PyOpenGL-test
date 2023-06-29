from src.GameObject import GameObject
from src.math.Vector3 import Vector3


class PhysicsBody(GameObject):
    def __init__(self, drag=0.0001, mass=1):
        self.transform = None
        self.velocity = Vector3(0, 0, 0)
        self.drag = drag
        self.mass = mass
        self.grounded = False

    def initialize(self):
        self.transform = self.components["Transform"]

    def update(self):
        if not self.grounded:
            self.velocity.y = self.velocity.y + (0.00008 * self.mass)

            if self.velocity.y > self.drag:
                self.velocity.y = self.drag

        self.transform.position -= self.velocity

    def apply_force(self, force):
        self.velocity = self.velocity + force
