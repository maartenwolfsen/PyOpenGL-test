from src.Vector3 import Vector3


class Ray:
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction

    def intersect_ray_collider(self, collider):
        inv_scale = Vector3(1 / collider.transform.scale.x, 1 / collider.transform.scale.y, 1 / collider.transform.scale.z)
        local_origin = (self.origin - collider.transform.position) * inv_scale
        local_direction = self.direction * inv_scale

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

        return not (t_enter > t_exit or t_exit < 0)
