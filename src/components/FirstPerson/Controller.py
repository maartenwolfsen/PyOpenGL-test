from src.GameObject import GameObject
from src.math.Vector2 import Vector2
from src.math.Vector3 import Vector3
import math


class Controller(GameObject):
    def __init__(self, speed=0.00005):
        self.speed = speed
        self.jumped = False
        self.jump_force = -0.02
        self.move_vectors = Vector2(0.0, 0.0)

    def update(self):
        camera = self.components["Camera"]
        forward_vector = math.radians(camera.yaw)
        strafe_vector = math.radians(camera.yaw + 90)
        movement_vector = (
            (Vector3(-math.sin(forward_vector), 0, -math.cos(forward_vector)) * -self.move_vectors.y * self.speed)
            + (Vector3(-math.sin(strafe_vector), 0, -math.cos(strafe_vector)) * -self.move_vectors.x * self.speed)
        )
        movement_vector.y = 0

        self.components["PhysicsBody"].apply_force(movement_vector)

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
