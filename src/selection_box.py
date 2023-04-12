""" Selection box class file """
import pygame
import src.config as cfg


class SelectionBox:
    """ Selection box class that moves towards selected crumb """

    def __init__(self, y):
        self.y = y
        self.x = 0
        self.color = cfg.PURPLE

        # Extract font dimensions
        self.chary = pygame.font.Font(cfg.chary_font, cfg.bit_string_font_size)
        bit_string_rect = self.chary.render(cfg.bit_string, True, self.color).get_rect()
        self.char_width = bit_string_rect.width / len(cfg.bit_string)
        self.char_height = bit_string_rect.height

    def draw(self, screen):
        """
        Draws selection box onto screen
        :param screen:
        :return:
        """
        self.calculate_index_x()
        if cfg.game_state == "game_over" and len(cfg.bit_string) < 2:
            x = cfg.screen_width / 2 - self.char_width
            pygame.draw.rect(screen, self.color, pygame.Rect(x, self.y, self.char_width * 2, self.char_height), 8)
        else:
            pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.char_width * 2, self.char_height), 8)

    def calculate_index_x(self):
        """
        Calculates index x pixel position according to current index
        :return:
        """
        # Extract bit string font rect and dimensions
        chary = pygame.font.Font(cfg.chary_font, cfg.bit_string_font_size)
        bit_string_rect = chary.render(cfg.bit_string, True, self.color).get_rect()

        # Centers the starting x position according to the screen width
        starting_x = cfg.screen_width / 2 - bit_string_rect.width / 2
        self.x = starting_x + cfg.index * self.char_width
