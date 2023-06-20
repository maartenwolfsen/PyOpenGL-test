import glfw
from OpenGL.GL import *
from src.Scene import Scene
from src.Player import Player
from src.math.Vector3 import Vector3
from src.components.Transform import Transform
from src.Camera import Camera
from src.Display import Display
from src.InputManager import InputManager

DEBUG = False

display = Display(800, 600)
player = Player()
camera = Camera()
scene = Scene("world1")
input_manager = InputManager(player, camera, scene)


def main():
    while not glfw.window_should_close(display.screen):
        glfw.poll_events()

        if player.velocity.y < player.drag:
            player.velocity.y += player.gravity

        collide = False

        for o in scene.game_objects:
            if hasattr(o, "collider") and o.collider.is_colliding(
                    Transform(
                        Vector3(
                            player.transform.position.x,
                            player.transform.position.y - player.velocity.y,
                            player.transform.position.z
                        ),
                        player.transform.rotation,
                        player.transform.scale
                    )
            ):
                collide = True
                break

        player.grounded = False

        if collide:
            player.velocity.y = 0
            player.grounded = True
            player.jumped = False

        glfw.set_input_mode(display.screen, glfw.STICKY_KEYS, GL_TRUE)
        glfw.set_key_callback(display.screen, input_manager.key_event)
        glfw.set_mouse_button_callback(display.screen, input_manager.mouse_event)
        glfw.set_cursor_pos_callback(display.screen, input_manager.cursor_pos_event)
        player.move_player(camera, scene.game_objects)

        glClearColor(0, 0, 0, 0)
        scene.render(display, camera, player, DEBUG)


if __name__ == "__main__":
    main()
