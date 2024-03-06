# labyrint game
import arcade

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
SCREEN_TITLE = "DodgeBird"

PLAYER_SPEED = 6  # player speed
# mazen som bakgrund
class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.setup()
        self.run = True  # Starts the game
        # background
        self.bg = arcade.load_texture("assets/maze.png")  # loading different

    def on_draw(self):
        if self.run:
            self.clear()
            arcade.draw_texture_rectangle(SCREEN_WIDTH / 2,  # function for loading the background
                                          SCREEN_HEIGHT / 2, SCREEN_WIDTH,
                                          SCREEN_HEIGHT, self.bg)
# spelarens movement
    def movment(self):
        # players movment
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

# collision

# finish
    # add goal point for player to reach
    def add_goal_point(self, screen):
        # adding gate for the goal point
        img_path = 'assets/gate.png'
        img = arcade.load_texture(img_path)
        screen.blit(img, (self.goal_cell.x * self.tile, self.goal_cell.y * self.tile))

    # winning message
    def message(self):
        msg = self.font.render('You Win!!', True, self.message_color)
        return msg

    # checks if player reached the goal point
    def is_game_over(self, player):
        goal_cell_abs_x, goal_cell_abs_y = self.goal_cell.x * self.tile, self.goal_cell.y * self.tile
        if player.x >= goal_cell_abs_x and player.y >= goal_cell_abs_y:
            return True
        else:
            return False

# main så spelet fungerar