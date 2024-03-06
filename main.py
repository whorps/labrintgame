# labyrint game
    # python arcade library
    # https://thepythoncode.com/article/build-a-maze-game-in-python
    # daniels DodgeBird game
import arcade

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
SCREEN_TITLE = "Labyrint Game"

PLAYER_SPEED = 4

# mazen som bakgrund
    def background(self):
        # Background image will be stored in this variable
        self.background = None
        self.background = arcade.load_texture("assets/maze.jpg")
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                        SCREEN_WIDTH, SCREEN_HEIGHT,
                                        self.background)

# players movement
    def player_movement(self):
        # registers movement
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

# collision

# goal point for players to reach
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
    def setup(self):
        self.run = True

    window = SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE
    window.setup()

    arcade.run()