from src.GameObject import GameObject
from src.math.Vector2 import Vector2
from src.math.Vector3 import Vector3
from src.components.Transform import Transform
import math


class Controller(GameObject):
    def __init__(self, speed=0.005):
        self.speed = speed
        self.jumped = False
        self.jump_force = -0.02
        self.move_vectors = Vector2(0.0, 0.0)

    def update(self, game_objects):
        camera = self.components["Camera"]
        angle_forward = math.radians(camera.yaw)
        angle_strafe = math.radians(camera.yaw + 90)

        movement_vector = (
            Vector3(-math.sin(angle_forward), 0, -math.cos(angle_forward))
            * self.move_vectors.y
            + Vector3(-math.sin(angle_strafe), 0, -math.cos(angle_strafe)
        ) * self.move_vectors.x) * self.speed
        new_position = self.components["Transform"].position + movement_vector

        new = Transform(
            new_position,
            self.components["Transform"].rotation,
            self.components["Transform"].scale
        )

        if not self.is_colliding(game_objects, new):
            self.components["Transform"].position = new_position

        return

    def jump(self):
        if self.components["PhysicsBody"].grounded:
            self.components["PhysicsBody"].grounded = False
            self.components["PhysicsBody"].apply_force(Vector3(0, self.jump_force, 0))
            self.jumped = True

    def is_colliding(self, game_objects, new_position):
        for go in game_objects:
            if "Collider" in go.components and go.components["Collider"].is_colliding(new_position):
                return True
        return False
