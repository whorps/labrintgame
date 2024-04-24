import arcade
import numpy as np  # for image processing

# Information to prevent magic numbers
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


class Player():
    # Players movement
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


class LabyrinthGame(arcade.Window):
    # Background and player
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.background = arcade.load_texture("assets/maze.jpg")
        self.gate = Gate("assets/gate.png", GOAL_POINT_CORD_X, GOAL_POINT_CORD_Y, scale=0.115)
        self.player = Player()
        # Load maze image and convert it to a numpy array
        self.maze_image = arcade.load_texture("assets/maze.jpg").image
        self.maze_data = np.array(self.maze_image)

    def on_draw(self):
        # Render background and player
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.background)
        self.gate.draw()
        self.player.draw()

    def update(self, delta_time: float):
        # Update border, player, and gate
        self.borderCollision()
        self.gate.update()
        self.player.update()

    def borderCollision(self):
        # Check for collision with maze walls
        player_pos_x = int(self.player.center_x)
        player_pos_y = int(self.player.center_y)

        # Check if the player is inside the maze boundaries
        if (player_pos_x < 0 or player_pos_x >= SCREEN_WIDTH or
                player_pos_y < 0 or player_pos_y >= SCREEN_HEIGHT):
            return

        # Check if the player's position corresponds to a wall pixel
        # Use a threshold to determine if the pixel is considered a wall
        threshold = 100  # Adjust this value according to your maze image
        if self.maze_data[player_pos_y, player_pos_x, 0] < threshold:
            # Collision with a wall, revert player's position
            self.player.center_x -= self.player.change_x
            self.player.center_y -= self.player.change_y

    def on_key_press(self, symbol: int, modifiers: int):
        # When key pressed, change x, y
        if symbol == arcade.key.W:
            self.player.change_y += 2
        if symbol == arcade.key.S:
            self.player.change_y += -2
        if symbol == arcade.key.D:
            self.player.change_x += 2
        if symbol == arcade.key.A:
            self.player.change_x += -2

    def on_key_release(self, symbol: int, modifiers: int):
        # When key released, stop
        if symbol == arcade.key.W:
            self.player.change_y = 0
        if symbol == arcade.key.S:
            self.player.change_y = 0
        if symbol == arcade.key.D:
            self.player.change_x = 0
        if symbol == arcade.key.A:
            self.player.change_x = 0

# Start game
def main():
    LabyrinthGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()