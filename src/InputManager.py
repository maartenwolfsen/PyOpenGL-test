import glfw


class InputManager:
    def __init__(self, scene):
        self.scene = scene

    def key_event(self, window, key, scancode, action, mods):
        player = self.scene.get_game_object_by_component("Controller").components["Controller"]
        if action == glfw.PRESS:
            if key == glfw.KEY_ESCAPE:
                glfw.terminate()
                quit()
            """if key == glfw.KEY_SPACE and player.grounded and not player.jumped:
                player.velocity.y = -player.jump_force
                player.jumped = True"""
            if key == glfw.KEY_A:
                if player.move_vectors.x == -1.0:
                    player.move_vectors.x = 0
                else:
                    player.move_vectors.x = 1.0
            if key == glfw.KEY_D:
                if player.move_vectors.x == 1.0:
                    player.move_vectors.x = 0
                else:
                    player.move_vectors.x = -1.0
            if key == glfw.KEY_W:
                if player.move_vectors.y == -1.0:
                    player.move_vectors.y = 0
                else:
                    player.move_vectors.y = 1.0
            elif key == glfw.KEY_S:
                if player.move_vectors.y == 1.0:
                    player.move_vectors.y = 0
                else:
                    player.move_vectors.y = -1.0
        elif action == glfw.RELEASE:
            if key == glfw.KEY_A:
                if player.move_vectors.x == 0.0:
                    player.move_vectors.x = -1.0
                elif player.move_vectors.x == 1.0:
                    player.move_vectors.x = 0.0
            elif key == glfw.KEY_D:
                if player.move_vectors.x == 0.0:
                    player.move_vectors.x = 1.0
                elif player.move_vectors.x == -1.0:
                    player.move_vectors.x = 0.0
            elif key == glfw.KEY_W:
                if player.move_vectors.y == 0.0:
                    player.move_vectors.y = -1.0
                elif player.move_vectors.y == 1.0:
                    player.move_vectors.y = 0.0
            elif key == glfw.KEY_S:
                if player.move_vectors.y == 0.0:
                    player.move_vectors.y = 1.0
                elif player.move_vectors.y == -1.0:
                    player.move_vectors.y = 0.0

    def mouse_event(self, window, button, action, mods):
        if button == glfw.MOUSE_BUTTON_LEFT and action == glfw.PRESS:
            """ray = Ray(
                Vector3(
                    player.transform.position.x + (player.transform.scale.x / 2),
                    player.transform.position.y + (player.transform.scale.y / 2),
                    player.transform.position.z + (player.transform.scale.z / 2)
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

                    break"""

    def cursor_pos_event(self, window, xpos, ypos):
        camera = self.scene.get_game_object_by_component("Camera").components["Camera"]
        mouse_x, mouse_y = glfw.get_cursor_pos(window)
        mouse_movement_x = mouse_x - camera.last_mouse_x
        mouse_movement_y = mouse_y - camera.last_mouse_y
        camera.last_mouse_x = mouse_x
        camera.last_mouse_y = mouse_y

        camera.move((mouse_movement_x, mouse_movement_y))
