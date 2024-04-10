# labyrint game
# python arcade library
# https://thepythoncode.com/article/build-a-maze-game-in-python
# daniels DodgeBird game
import arcade

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
SCREEN_TITLE = "Labyrint Game"

PLAYER_SPEED = 4
PLAYER_WIDTH = 35
PLAYER_HEIGHT = 35
PLAYER_COLOR = arcade.color.DARK_BROWN

class Player():
    # players movement
    def __init__(self):
        self.center_x = 85
        self.center_y = 85
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


class LabyrintGame(arcade.Window):
    # bakgrund
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        """Background"""
        self.background = arcade.load_texture("assets/maze.jpg")
        self.player = Player()



    def on_draw(self):
        arcade.start_render()
        """Background"""
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.background)
        self.player.draw()

    # collision förbättra
    def borderCollisison(self):
        # provents to travel outside the screen
        if self.center_y <= 20:
            self.center_y = 20
        if self.center_y >= SCREEN_HEIGHT:
            self.center_y = SCREEN_HEIGHT
        if self.center_x <= 0:
            self.center_x = 0
        if self.center_x >= SCREEN_WIDTH:
            self.center_x = SCREEN_WIDTH

    # goal point for players to reach
    def add_goal_point(self, screen):
        # adding gate for the goal point
        img_path = 'assets/gate.png'
        img = arcade.load_texture(img_path)
        screen.blit(img, (self.goal_cell.x * self.tile, self.goal_cell.y * self.tile))

    # winning message when reaching goal point
    def message(self):
        msg = self.font.render('You Win!!', True, self.message_color)
        return msg

    # checks if player reached the goal point
    #gör det snyggare
    def is_game_over(self, player):
        goal_cell_abs_x, goal_cell_abs_y = self.goal_cell.x * self.tile, self.goal_cell.y * self.tile
        if player.x >= goal_cell_abs_x and player.y >= goal_cell_abs_y:
            return True
        else:
            return False

    # starts game

def main():
    LabyrintGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()
