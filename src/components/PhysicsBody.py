from src.GameObject import GameObject
from src.math.Vector3 import Vector3
from src.components.Transform import Transform


class PhysicsBody(GameObject):
    def __init__(self, drag=0.005, mass=1):
        self.velocity = Vector3(0, 0, 0)
        self.drag = drag
        self.mass = mass
        self.grounded = False

    def update(self, label, game_objects):
        if not self.grounded:
            self.velocity.y = self.velocity.y + (0.00008 * self.mass)

            if self.velocity.y > self.drag:
                self.velocity.y = self.drag

        new_t = Transform(
            self.components["Transform"].position,
            self.components["Transform"].rotation,
            self.components["Transform"].scale
        )
        new_t.position -= self.velocity
        is_colliding = False

        for game_object in game_objects:
            if (
                label != game_object.label
                and "Collider" in game_object.components
                and game_object.components["Collider"].is_colliding(new_t)
            ):
                is_colliding = True
                break

        if not is_colliding:
            self.components["Transform"] = new_t

    def apply_force(self, force):
        self.velocity = self.velocity + force
