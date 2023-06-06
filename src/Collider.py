class Collider:
    def __init__(self, transform):
        self.transform = transform

    def is_colliding(self, collider):
        object1_min = self.transform.position - 0.5 * self.transform.scale
        object1_max = self.transform.position + 0.5 * self.transform.scale
        object2_min = collider.transform.position - 0.5 * collider.transform.scale
        object2_max = collider.transform.position + 0.5 * collider.transform.scale

        if (object1_max.x >= object2_min.x and object1_min.x <= object2_max.x) and \
                (object1_max.y >= object2_min.y and object1_min.y <= object2_max.y) and \
                (object1_max.z >= object2_min.z and object1_min.z <= object2_max.z):
            return True
        else:
            return False
