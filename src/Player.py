from src.math.Vector3 import Vector3
from src.components.Transform import Transform
import math


class Player:
    def __init__(self):
        self.transform = Transform(
            Vector3(0, 0, 0),
            Vector3(0, 0, 0),
            Vector3(1, 1, 1)
        )
        self.velocity = Vector3(0, 0, 0)
        self.drag = 0.5
        self.jump_force = 0.1
        self.grounded = True
        self.jumped = False
        self.gravity = 0.005
        self.speed = 0.05

    def move_player(self, direction, camera, game_objects):
        angle = math.radians(camera.yaw - 90) if direction in ['a', 'd'] else math.radians(camera.yaw)
        if direction in ['w', 'd']:
            angle += math.pi
        new_x = self.transform.position.x + self.speed * math.sin(angle)
        new_z = self.transform.position.z + self.speed * math.cos(angle)
        temp_collider = Transform(
            Vector3(new_x, self.transform.position.y, new_z),
            self.transform.rotation,
            self.transform.scale
        )

        collide = False
        for o in game_objects:
            if hasattr(o, "collider") and o.collider.is_colliding(temp_collider):
                collide = True
                break

        if not collide:
            self.transform.position.x = new_x
            self.transform.position.z = new_z
