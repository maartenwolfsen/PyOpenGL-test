from src.math.Vector2 import Vector2
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
        self.move_vectors = Vector2(0.0, 0.0)
        self.velocity = Vector3(0, 0, 0)
        self.drag = 0.5
        self.jump_force = 0.015
        self.grounded = True
        self.jumped = False
        self.speed = 0.005

    def move_player(self, camera, game_objects):
        movement_direction = self.determine_movement_direction(self.move_vectors)

        if movement_direction:
            forward_vector = self.calculate_forward_vector(camera.yaw)
            strafe_vector = self.calculate_strafe_vector(camera.yaw)
            movement_vector = forward_vector * self.move_vectors.y + strafe_vector * self.move_vectors.x
            movement_vector = self.scale_vector(movement_vector, self.speed)
            new_position = self.transform.position + movement_vector

            if not self.is_collision_detected(game_objects, new_position):
                self.update_player_position(self.transform, new_position)

        #self.update_player_vertical_position(self.transform, self.velocity.y)

    def calculate_forward_vector(self, yaw):
        angle = math.radians(yaw)
        return Vector3(-math.sin(angle), 0, -math.cos(angle))

    def calculate_strafe_vector(self, yaw):
        angle = math.radians(yaw + 90)
        return Vector3(-math.sin(angle), 0, -math.cos(angle))

    def scale_vector(self, vector, scale):
        return vector * scale

    def determine_movement_direction(self, move_vectors):
        if move_vectors.x == -1.0:
            return 'a'
        elif move_vectors.x == 1.0:
            return 'd'
        elif move_vectors.y == -1.0:
            return 'w'
        elif move_vectors.y == 1.0:
            return 's'
        else:
            return ''

    def is_collision_detected(self, game_objects, new_position):
        temp_collider = self.create_temporary_collider(new_position)
        for game_object in game_objects:
            if hasattr(game_object, "collider") and game_object.collider.is_colliding(temp_collider):
                return True
        return False

    def create_temporary_collider(self, new_position):
        return Transform(new_position, self.transform.rotation, self.transform.scale)

    def update_player_position(self, transform, new_position):
        transform.position = new_position

    def update_player_vertical_position(self, transform, velocity_y):
        transform.position.y -= velocity_y
