from src.Vector3 import Vector3


class Ray:
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction.normalize()

    def intersect_ray_collider(self, collider):
        inv_scale = Vector3(1 / collider.scale.x, 1 / collider.scale.y, 1 / collider.scale.z)
        local_origin = (self.origin - collider.position) * inv_scale
        local_direction = self.direction * inv_scale

        tin = Vector3(float("-inf"))
        tax = Vector3(float("inf"))

        if local_direction.x != 0:
            tin.x = (Vector3(-0.5) - local_origin.x) / local_direction.x
            tax.x = (Vector3(0.5) - local_origin.x) / local_direction.x

        if local_direction.y != 0:
            tin.y = (Vector3(-0.5) - local_origin.y) / local_direction.y
            tax.y = (Vector3(0.5) - local_origin.y) / local_direction.y

        if local_direction.z != 0:
            tin.z = (Vector3(-0.5) - local_origin.z) / local_direction.z
            tax.z = (Vector3(0.5) - local_origin.z) / local_direction.z

        if min(tax.x, tax.y, tax.z) >= max(tin.x, tin.y, tin.z) >= 0:
            return True

        return False

