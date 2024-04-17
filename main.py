# labyrint game
# python arcade library
# https://thepythoncode.com/article/build-a-maze-game-in-python
# daniels DodgeBird game
import arcade

# information to provent magic numbers
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
SCREEN_TITLE = "Labyrint Game"

GOAL_POINT_CORD_X = 667
GOAL_POINT_CORD_Y = 321

PLAYER_WIDTH = 35
PLAYER_HEIGHT = 35
PLAYER_COLOR = arcade.color.ARMY_GREEN
START_COORD_X = 85
START_COORD_Y = 85


class Player():
    # players movement
    def __init__(self):
        self.center_x = START_COORD_X
        self.center_y = START_COORD_Y
        self.change_x = 0
        self.change_y = 0

    def update(self):
        # Update player position based on pressed keys
        self.center_x += self.change_x
        self.center_y += self.change_y

    def draw(self):
        # Draw the player
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

    # Override the draw method to use the loaded texture
    def draw(self):
        super().draw()


class LabyrintGame(arcade.Window):
    # background and player
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.background = arcade.load_texture("assets/maze.jpg")
        self.gate = Gate("assets/gate.png", GOAL_POINT_CORD_X, GOAL_POINT_CORD_Y, scale=0.115)
        self.player = Player()

    def on_draw(self):
        # render background and player
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.background)
        self.gate.draw()
        self.player.draw()

    def update(self, delta_time: float):
        # update border, player and gate
        self.borderCollisison()
        self.gate.update()
        self.player.update()

    # border collision
    def borderCollisison(self):
        # provents to travel outside the screen
        if self.player.center_y <= 20:
            self.player.center_y = 20
        if self.player.center_y >= SCREEN_HEIGHT:
            self.player.center_y = SCREEN_HEIGHT
        if self.player.center_x <= 0:
            self.player.center_x = 0
        if self.player.center_x >= SCREEN_WIDTH:
            self.player.center_x = SCREEN_WIDTH

    def on_key_press(self, symbol: int, modifiers: int):
        # when key pressed change x, Y
        if symbol == arcade.key.W:
            self.player.change_y += 2
        if symbol == arcade.key.S:
            self.player.change_y += -2
        if symbol == arcade.key.D:
            self.player.change_x += 2
        if symbol == arcade.key.A:
            self.player.change_x += -2

    def on_key_release(self, symbol: int, modifiers: int):
        # when key released. stop
        if symbol == arcade.key.W:
            self.player.change_y = 0
        if symbol == arcade.key.S:
            self.player.change_y = 0
        if symbol == arcade.key.D:
            self.player.change_x = 0
        if symbol == arcade.key.A:
            self.player.change_x = 0

# starts game
def main():
    LabyrintGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()
