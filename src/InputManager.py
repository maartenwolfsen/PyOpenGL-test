import glfw
from src.Ray import Ray
from src.math.Vector3 import Vector3
from src.GameObject import GameObject
from src.primitives.Cube import Cube
from src.components.Collider import Collider
from src.components.Transform import Transform


class InputManager:
    def __init__(self, player, camera, scene):
        self.player = player
        self.camera = camera
        self.scene = scene

    def key_event(self, window, key, scancode, action, mods):
        if action == glfw.PRESS:
            if key == glfw.KEY_ESCAPE:
                glfw.terminate()
                quit()
            if key == glfw.KEY_SPACE and self.player.grounded and not self.player.jumped:
                self.player.velocity.y = -self.player.jump_force
                self.player.jumped = True
            if key == glfw.KEY_A:
                if self.player.move_vectors.x == -1.0:
                    self.player.move_vectors.x = 0
                else:
                    self.player.move_vectors.x = 1.0
            if key == glfw.KEY_D:
                if self.player.move_vectors.x == 1.0:
                    self.player.move_vectors.x = 0
                else:
                    self.player.move_vectors.x = -1.0
            if key == glfw.KEY_W:
                if self.player.move_vectors.y == -1.0:
                    self.player.move_vectors.y = 0
                else:
                    self.player.move_vectors.y = 1.0
            elif key == glfw.KEY_S:
                if self.player.move_vectors.y == 1.0:
                    self.player.move_vectors.y = 0
                else:
                    self.player.move_vectors.y = -1.0
        elif action == glfw.RELEASE:
            if key == glfw.KEY_A:
                if self.player.move_vectors.x == 0.0:
                    self.player.move_vectors.x = -1.0
                elif self.player.move_vectors.x == 1.0:
                    self.player.move_vectors.x = 0.0
            elif key == glfw.KEY_D:
                if self.player.move_vectors.x == 0.0:
                    self.player.move_vectors.x = 1.0
                elif self.player.move_vectors.x == -1.0:
                    self.player.move_vectors.x = 0.0
            elif key == glfw.KEY_W:
                if self.player.move_vectors.y == 0.0:
                    self.player.move_vectors.y = -1.0
                elif self.player.move_vectors.y == 1.0:
                    self.player.move_vectors.y = 0.0
            elif key == glfw.KEY_S:
                if self.player.move_vectors.y == 0.0:
                    self.player.move_vectors.y = 1.0
                elif self.player.move_vectors.y == -1.0:
                    self.player.move_vectors.y = 0.0

    def mouse_event(self, window, button, action, mods):
        if button == glfw.MOUSE_BUTTON_LEFT and action == glfw.PRESS:
            ray = Ray(
                Vector3(
                    self.player.transform.position.x + (self.player.transform.scale.x / 2),
                    self.player.transform.position.y + (self.player.transform.scale.y / 2),
                    self.player.transform.position.z + (self.player.transform.scale.z / 2)
                ),
                self.camera.get_direction()
            )

            for o in self.scene.game_objects:
                hit = ray.intersect_ray_collider(o.collider)

                if hit is not None:
                    t = Transform(
                        hit,
                        Vector3(0, 0, 0),
                        Vector3(0.5, 0.5, 0.5)
                    )
                    self.scene.add(
                        GameObject(
                            "hit" + str(ray.count),
                            t,
                            Cube(),
                            Collider(t)
                        )
                    )

                    for x in self.scene.game_objects:
                        print(x.id)
                        print(x.transform.position)

                    break

    def cursor_pos_event(self, window,  xpos, ypos):
        mouse_x, mouse_y = glfw.get_cursor_pos(window)
        mouse_movement_x = mouse_x - self.camera.last_mouse_x
        mouse_movement_y = mouse_y - self.camera.last_mouse_y
        self.camera.last_mouse_x = mouse_x
        self.camera.last_mouse_y = mouse_y

        self.camera.move((mouse_movement_x, mouse_movement_y))
