import glfw
from OpenGL.GL import *
from src.Scene import Scene
from src.Display import Display
from src.InputManager import InputManager

DEBUG = False

display = Display(800, 600)
scene = Scene("world1")
input_manager = InputManager(scene)


def main():
    while not glfw.window_should_close(display.screen):
        glClearColor(0, 0, 0, 0)

        glfw.poll_events()
        glfw.set_input_mode(display.screen, glfw.STICKY_KEYS, GL_TRUE)
        glfw.set_key_callback(display.screen, input_manager.key_event)
        glfw.set_mouse_button_callback(display.screen, input_manager.mouse_event)
        glfw.set_cursor_pos_callback(display.screen, input_manager.cursor_pos_event)

        scene.render(display, DEBUG)


if __name__ == "__main__":
    main()
