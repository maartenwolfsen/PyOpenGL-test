class PlayerController:
    def __init__(self, speed=0.005):
        self.speed = speed
        self.jumped = False

    def move(self):
        return False
