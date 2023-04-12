""" Global Variables """
import pygame

# Screen dimensions (the UI does not support responsive design, DO NOT CHANGE)
screen_width = 800
screen_height = 500

# Hex colors (Entomophobia)
HEX_BLUE = "#212236"
HEX_RED = "#73303e"
HEX_PURPLE = "#794e6b"
HEX_TEAL = "#527a76"
HEX_GREEN = "#6d8560"
HEX_BROWN = "#a3866b"
HEX_YELLOW = "#c99c69"
HEX_WHITE = "#d0c4bd"

# Pygame colors
BLUE = pygame.Color(HEX_BLUE)
RED = pygame.Color(HEX_RED)
PURPLE = pygame.Color(HEX_PURPLE)
TEAL = pygame.Color(HEX_TEAL)
GREEN = pygame.Color(HEX_GREEN)
BROWN = pygame.Color(HEX_BROWN)
YELLOW = pygame.Color(HEX_YELLOW)
WHITE = pygame.Color(HEX_WHITE)

# Font
chary_font = "fonts/chary.ttf"

# Scores
p1_score = 0
p2_score = 0
pc_score = 0

# Opponent
opponent = "player"
opponent_list = [1, ["player", "computer"]]
whose_turn = "p1"  # "p1", "p2", "pc"
whose_first = "player"  # "player", "computer"

# Bit string
bit_string = ""
bit_string_font_size = 80

# Difficulty (string length)
EASY = 6
MEDIUM = 8
HARD = 10
difficulty_list = [2, [EASY, MEDIUM, HARD]]  # difficulty list for toggles
difficulty = MEDIUM  # default difficulty

# Selection box
index = 0
index_x = 0

# Logic
game_state = "game_over"  # "playing", "game_over"
is_marked = False
last_time = 0
prev = 0
target_index = 0
