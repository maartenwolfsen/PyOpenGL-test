class Ray:
    count = 0

    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction.normalize()
        Ray.count += 1
        print(self.origin)
        print(self.direction)

    def intersect_ray_collider(self, collider):
        min_bounds, max_bounds = collider.bounds

        tmin = (min_bounds[0] - self.origin[0]) / self.direction[0]
        tmax = (max_bounds[0] - self.origin[0]) / self.direction[0]

        if tmin > tmax:
            tmin, tmax = tmax, tmin

        tymin = (min_bounds[1] - self.origin[1]) / self.direction[1]
        tymax = (max_bounds[1] - self.origin[1]) / self.direction[1]

        if tymin > tymax:
            tymin, tymax = tymax, tymin

        if (tmin > tymax) or (tymin > tmax):
            return None

        if tymin > tmin:
            tmin = tymin

        if tymax < tmax:
            tmax = tymax

        if tmax < 0:
            return None

        point_of_contact = self.origin + tmin * self.direction
        return point_of_contact

