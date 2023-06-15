from src.Vector3 import Vector3
from src.Quaternion import Quaternion


class Ray:
    count = 0

    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction
        Ray.count += 1

    def intersect_ray_collider(self, collider):
        inv_scale = Vector3(
            1 / collider.transform.scale.x,
            1 / collider.transform.scale.y,
            1 / collider.transform.scale.z
        )

        rotation = collider.transform.rotation
        rotation_mag = rotation.magnitude()
        if rotation_mag == 0:
            return None

        inv_rotation = Quaternion.inverse(rotation)

        local_origin = self.origin - collider.transform.position
        local_direction = self.direction

        # Rotate the origin and direction using the inverse rotation quaternion
        local_origin = inv_rotation.rotate(local_origin)
        local_direction = inv_rotation.rotate(local_direction)

        # Apply inverse scaling to the rotated origin and direction
        local_origin *= inv_scale
        local_direction *= inv_scale

        t_min = Vector3(float("-inf"))
        t_max = Vector3(float("inf"))

        for i in range(3):
            if local_direction[i] != 0:
                t1 = (collider.bounds[0][i] - local_origin[i]) / local_direction[i]
                t2 = (collider.bounds[1][i] - local_origin[i]) / local_direction[i]
                t_min[i] = min(t1, t2)
                t_max[i] = max(t1, t2)

        t_enter = max(t_min)
        t_exit = min(t_max)

        if t_enter > t_exit or t_exit < 0:
            return None

        intersection_point = self.origin + self.direction * t_enter
        return intersection_point


