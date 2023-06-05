class GameObject:
    def __init__(self, transform, mesh, collider):
        self.transform = transform
        self.mesh = mesh
        self.collider = collider

    def draw(self):
        self.mesh.draw(self.transform)
