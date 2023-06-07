from src.Vector3 import Vector3
from src.components.Transform import Transform
import math


class Player:
    def __init__(self):
        self.transform = Transform(
            Vector3(0, 0, 0),
            Vector3(0, 0, 0),
            Vector3(1, 1, 1)
        )

        self.speed = 0.05

    def move_player(self, direction, camera, game_objects):
        angle = math.radians(camera.yaw - 90) if direction in ['a', 'd'] else math.radians(camera.yaw)
        if direction in ['w', 'd']:
            angle += math.pi
        new_x = self.transform.position.x + self.speed * math.sin(angle)
        new_z = self.transform.position.z + self.speed * math.cos(angle)
        temp_collider = Transform(Vector3(new_x, self.transform.position.y, new_z), self.transform.rotation,
                                  self.transform.scale)

        collide = False
        slide_vector = Vector3(0, 0, 0)
        num_collisions = 0

        for o in game_objects:
            if o.collider.is_colliding(temp_collider):
                collide = True
                num_collisions += 1

                collision_vector = temp_collider.position - o.collider.transform.position
                collision_vector.y = 0
                collision_vector = collision_vector.normalize()

                slide_vector += collision_vector

        if collide:
            if num_collisions > 0:
                slide_vector = slide_vector.normalize() * (
                            self.speed * 0.1 * num_collisions)

            self.transform.position.x += slide_vector.x
            self.transform.position.z += slide_vector.z
        else:
            self.transform.position.x = new_x
            self.transform.position.z = new_z
