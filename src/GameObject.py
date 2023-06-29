class GameObject:
    components = {}

    def __init__(self, label, mesh, *args):
        self.label = label
        self.mesh = mesh

        for c in args:
            self.components[type(c).__name__] = c
            c.components = self.components
            if hasattr(c, "initialize"):
                c.initialize()

    def draw(self):
        self.mesh.draw(self.components["Transform"])

    def has(self, component):
        return component in self.components
