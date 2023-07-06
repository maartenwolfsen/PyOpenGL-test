class PhysicsWorld():
    def __init__(self, scene):
        self.scene = scene
        self.gravity = 0.00003
        self.drag = 0.005

    def update(self):
        for go in self.scene.game_objects:
            if go.has("PhysicsBody"):
                go.components["PhysicsBody"].update(go.label, self.scene.game_objects, self.gravity, self.drag)
