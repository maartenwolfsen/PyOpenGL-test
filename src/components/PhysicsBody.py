from src.GameObject import GameObject
from src.math.Vector3 import Vector3
from src.components.Transform import Transform


class PhysicsBody(GameObject):
    def __init__(self, mass=1):
        self.velocity = Vector3(0, 0, 0)
        self.mass = mass
        self.grounded = False

    def update(self, label, game_objects, gravity, drag):
        if not self.grounded:
            self.velocity.y = self.velocity.y + (gravity * self.mass)

            if self.velocity.y > drag:
                self.velocity.y = drag

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
                if not self.grounded:
                    self.grounded = True
                    self.velocity = Vector3(0, 0, 0)

                is_colliding = True
                break

        if not is_colliding:
            self.components["Transform"] = new_t

    def apply_force(self, force):
        self.velocity = self.velocity + force
