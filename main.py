import pygame
import sys

import src.config as cfg
import src.util as util
import src.button as btn
import src.arrow_button as abtn
import src.text as txt
import src.selection_box as sb

# Initialize pygame
pygame.init()
clock = pygame.time.Clock()

# Initiate screen dimensions (the UI does not support responsive design, DO NOT CHANGE)
cfg.screen_width = 800
cfg.screen_height = 500
screen = pygame.display.set_mode((cfg.screen_width, cfg.screen_height))

# Set caption, icon
pygame.display.set_caption("Praktiskais darbs 1")
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)


class Program:
    """ Program Class """

    def __init__(self):
        # Initiate buttons
        self.select_button = btn.SelectButton("", 64, 52, (368, 288), cfg.RED)
        self.restart_button = btn.RestartButton("Restart", 105, 48, (348, 424), cfg.PURPLE, 30)
        self.opponent_toggle_button = btn.OpponentToggleButton("Player", 105, 48, (223, 424), cfg.GREEN, 30)
        self.difficulty_toggle_button = btn.DifficultyToggleButton("Medium", 105, 48, (473, 424), cfg.YELLOW, 30)
        self.whose_turn_button = btn.WhoseFirstButton("Player First", 105, 24, (223, 388), cfg.RED, 15)
        self.left_button = abtn.LeftButton("", 125, 80, (223, 276), cfg.PURPLE, direction="left")
        self.right_button = abtn.RightButton("", 125, 80, (452, 276), cfg.PURPLE, direction="right")

        # Generate random bit string
        util.generate_new_bit_string()

        # Set starting index
        util.reset_index()

        # Initiate selection box
        self.selection_box = sb.SelectionBox(144)

        # Initiate text
        self.p1_score_text = txt.ScoreText(44, 170, "P1", cfg.WHITE)
        self.p2_score_text = txt.ScoreText(684, 170, "P2", cfg.WHITE)
        self.pc_score_text = txt.ScoreText(684, 170, "PC", cfg.WHITE)
        self.bit_string_text = txt.BitStringText(144)
        self.win_text = txt.WinText(48)

    def run(self):
        """
        Runs program methods
        :return:
        """
        # Do logic
        util.check_win_condition()
        util.computer_moves()

        # Draw buttons
        self.select_button.draw(screen)
        self.restart_button.draw(screen)
        self.opponent_toggle_button.draw(screen)
        self.difficulty_toggle_button.draw(screen)
        self.whose_turn_button.draw(screen)
        self.left_button.draw(screen)
        self.right_button.draw(screen)

        # Draw side boxes
        pygame.draw.rect(screen, cfg.RED, pygame.Rect(0, 0, 160, 500))
        if cfg.opponent == "player":
            pygame.draw.rect(screen, cfg.GREEN, pygame.Rect(640, 0, 160, 500))
        else:
            pygame.draw.rect(screen, cfg.YELLOW, pygame.Rect(640, 0, 160, 500))

        # Draw scores
        self.p1_score_text.draw(screen, cfg.p1_score)
        if cfg.opponent == "player":
            self.p2_score_text.draw(screen, cfg.p2_score)
        else:
            self.pc_score_text.draw(screen, cfg.pc_score)

        # Draw bit string
        self.bit_string_text.draw(screen)

        # Draw selection box
        self.selection_box.draw(screen)

        # Draw win text
        self.win_text.draw(screen)


def main():

    # Initiate instances
    program = Program()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Run program
        program.run()

        # Updates
        pygame.display.flip()
        screen.fill(cfg.WHITE)


if __name__ == '__main__':
    main()
