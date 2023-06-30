class GameObject:
    count = 0

    def __init__(self, label, *args):
        self.label = label
        self.count = self.__class__.count
        self.components = {}

        for c in args:
            self.components[type(c).__name__] = c

        for c in self.components:
            self.components[c].components = self.components
            if hasattr(c, "initialize"):
                c.initialize()

        self.__class__.count += 1

    def draw(self):
        # TODO: Create a Mesh class
        print(self.count)
        print(self.components["Cube"])
        self.components["Cube"].draw(self.components["Transform"])

    def has(self, component):
        return component in self.components
