class Collider:
    def __init__(self, transform):
        self.transform = transform

    def is_colliding(self, collider):
        return (self.transform.position.x < collider.transform.position.x + collider.transform.scale.x
                and self.transform.position.x + self.transform.scale.x > collider.transform.position.x
                and self.transform.position.y < collider.transform.position.y + collider.transform.scale.y
                and self.transform.position.y + self.transform.scale.y > collider.transform.position.y
                and self.transform.position.z < collider.transform.position.z + collider.transform.scale.z
                and self.transform.position.z + self.transform.scale.z > collider.transform.position.z
                )
