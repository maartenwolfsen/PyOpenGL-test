class GameObject:
    def __init__(self, id, transform, mesh, collider):
        self.id = id
        self.transform = transform
        self.mesh = mesh
        self.collider = collider

    def draw(self):
        self.mesh.draw(self.transform)
