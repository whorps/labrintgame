# collision med svarta väggar är ett helvete
# Olle jag fattar fan inte vad jag ska göra
# men jag och chat gpt har gjort vårt bästa

import arcade
import numpy as np
from PIL import Image

# saker
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
SCREEN_TITLE = "Labyrinth Game"

GOAL_POINT_CORD_X = 667
GOAL_POINT_CORD_Y = 321

PLAYER_WIDTH = 35
PLAYER_HEIGHT = 35
PLAYER_COLOR = arcade.color.ARMY_GREEN
START_COORD_X = 85
START_COORD_Y = 85
PLAYER_SPEED = 2

class Player(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.center_x = START_COORD_X
        self.center_y = START_COORD_Y
        self.change_x = 0
        self.change_y = 0

        # hitbox
        self.set_hit_box([
            (-PLAYER_WIDTH // 2, -PLAYER_HEIGHT // 2),
            (PLAYER_WIDTH // 2, -PLAYER_HEIGHT // 2),
            (PLAYER_WIDTH // 2, PLAYER_HEIGHT // 2),
            (-PLAYER_WIDTH // 2, PLAYER_HEIGHT // 2),
        ])

    def update(self, maze_data):
        # Beräkna ny position
        new_x = self.center_x + self.change_x
        new_y = self.center_y + self.change_y

        # Kontrollera collision med väggar
        if not self.is_colliding_with_wall(new_x, new_y, maze_data):
            self.center_x = new_x
            self.center_y = new_y

        # collision med windowfliken
        if self.center_x < PLAYER_WIDTH / 2:
            self.center_x = PLAYER_WIDTH / 2
        if self.center_x > SCREEN_WIDTH - PLAYER_WIDTH / 2:
            self.center_x = SCREEN_WIDTH - PLAYER_WIDTH / 2
        if self.center_y < PLAYER_HEIGHT / 2:
            self.center_y = PLAYER_HEIGHT / 2
        if self.center_y > SCREEN_HEIGHT - PLAYER_HEIGHT / 2:
            self.center_y = SCREEN_HEIGHT - PLAYER_HEIGHT / 2

    def is_colliding_with_wall(self, x, y, maze_data):
        # Konvertera spelarens position till pixelindex
        left = int(x - PLAYER_WIDTH / 2)
        right = int(x + PLAYER_WIDTH / 2)
        bottom = int(y - PLAYER_HEIGHT / 2)
        top = int(y + PLAYER_HEIGHT / 2)

        # Kontrollera om spelarens hörn är i en vägg
        for ix in range(left, right):
            for iy in range(bottom, top):
                if maze_data[iy, ix] == 0:
                    return True
        return False

    def draw(self):
        # Rita spelaren
        arcade.draw_rectangle_filled(self.center_x,
                                     self.center_y,
                                     PLAYER_WIDTH,
                                     PLAYER_HEIGHT,
                                     PLAYER_COLOR)

class Gate(arcade.Sprite):
    def __init__(self, texture_file_path, center_x, center_y, scale=1.0):
        super().__init__(texture_file_path, scale=scale)
        self.center_x = center_x
        self.center_y = center_y

    def draw(self):
        super().draw()

class LabyrinthGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.background = arcade.load_texture("assets/maze.jpg")
        self.gate = Gate("assets/gate.png", GOAL_POINT_CORD_X, GOAL_POINT_CORD_Y, scale=0.115)
        self.player = Player()
        self.win = False
        # Ladda labyrintbilden och konvertera den till en numpy-array
        self.maze_image = Image.open("assets/maze.jpg").convert("L")  # Konvertera till gråskala
        self.maze_data = np.array(self.maze_image)

    def on_draw(self):
        # Rendera bakgrund, player och gate
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.background)
        self.gate.draw()
        self.player.draw()

        if self.win:
            arcade.draw_text("You Win!", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                             arcade.color.BLACK, 54, anchor_x="center")

    def update(self, delta_time: float):
        # Uppdatera spelare och kontrollera vinst
        if not self.win:
            self.player.update(self.maze_data)
            self.check_for_win()

    def check_for_win(self):
        if arcade.check_for_collision(self.player, self.gate):
            self.win = True
            self.player.change_x = 0
            self.player.change_y = 0

    def on_key_press(self, symbol: int, modifiers: int):
        # movement
        if not self.win:
            if symbol == arcade.key.W:
                self.player.change_y = PLAYER_SPEED
            if symbol == arcade.key.S:
                self.player.change_y = -PLAYER_SPEED
            if symbol == arcade.key.D:
                self.player.change_x = PLAYER_SPEED
            if symbol == arcade.key.A:
                self.player.change_x = -PLAYER_SPEED

    def on_key_release(self, symbol: int, modifiers: int):
        # När tangent släpps, stoppa
        if not self.win:
            if symbol in {arcade.key.W, arcade.key.S}:
                self.player.change_y = 0
            if symbol in {arcade.key.D, arcade.key.A}:
                self.player.change_x = 0

# Starta spelet
def main():
    LabyrinthGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()

if __name__ == "__main__":
    main()
