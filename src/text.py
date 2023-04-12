""" Text classes file """
import pygame
import src.config as cfg


class ScoreText:
    """ Score text class """

    def __init__(self, x, y, header_text, color):
        self.x = x
        self.y = y
        self.header_text = header_text
        self.color = color
        self.y_space = 80
        self.x_space = 15

        # Font
        self.chary = pygame.font.Font(cfg.chary_font, 80)

    def draw(self, screen, score):
        """
        Draws score text onto screen
        :param screen:
        :param score:
        :return:
        """
        header_text = self.chary.render(self.header_text, True, self.color)
        score_text = self.chary.render(str(score), True, self.color)
        screen.blit(header_text, (self.x, self.y))
        screen.blit(score_text, (self.x + self.x_space, self.y + self.y_space))


class BitStringText:
    """ Bit string text class """

    def __init__(self, y):
        self.y = y
        self.color = cfg.BLUE

    def draw(self, screen):
        """
        Draws bit string text onto screen
        :param screen:
        :return:
        """
        # font
        chary = pygame.font.Font(cfg.chary_font, cfg.bit_string_font_size)
        bit_string_text = chary.render(cfg.bit_string, True, self.color)
        x = cfg.screen_width / 2 - bit_string_text.get_width() / 2

        screen.blit(bit_string_text, (x, self.y))


class WinText:
    """ Win text class """

    def __init__(self, y):
        self.x = 0
        self.y = y

        # Font
        self.chary = pygame.font.Font(cfg.chary_font, 50)

    def draw(self, screen):
        """
        Draws score text onto screen
        :param screen:
        :return:
        """
        if cfg.game_state == "game_over":
            if cfg.opponent == "player":
                if cfg.p1_score == 0 and cfg.p2_score == 0:
                    win_text = ""
                    color = cfg.PURPLE
                elif cfg.p1_score > cfg.p2_score:
                    win_text = "Player 1 wins!"
                    color = cfg.RED
                elif cfg.p1_score < cfg.p2_score:
                    win_text = "Player 2 wins!"
                    color = cfg.GREEN
                else:
                    win_text = "Tied game!"
                    color = cfg.PURPLE
            else:
                if cfg.p1_score == 0 and cfg.pc_score == 0:
                    win_text = ""
                    color = cfg.PURPLE
                elif cfg.p1_score > cfg.pc_score:
                    win_text = "Player 1 wins!"
                    color = cfg.RED
                elif cfg.p1_score < cfg.pc_score:
                    win_text = "Computer wins!"
                    color = cfg.YELLOW
                else:
                    win_text = "Tied game!"
                    color = cfg.PURPLE

            # Centers win text according to screen width and text width
            text = self.chary.render(win_text, True, color)
            x = cfg.screen_width / 2 - text.get_width() / 2

            screen.blit(text, (x, self.y))
