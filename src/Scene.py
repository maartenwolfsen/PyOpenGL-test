class Scene:
    def __init__(self, name, game_objects):
        self.name = name
        self.game_objects = game_objects

    def add(self, game_object):
        self.game_objects.append(game_object)
