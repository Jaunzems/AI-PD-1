""" Class file for arrow button """
import pygame
import src.config as cfg


class ArrowButton:
    """ Arrow button abstract class """

    def __init__(self, text, width, height, pos, color, font_size=20, direction="left"):
        # Core attributes
        self.pressed = False
        self.disabled = False
        self.dir = direction
        self.elevation = 4
        self.dynamic_elevation = self.elevation
        self.text = text

        # Adjusted rect dimension
        self.rect_width = 3 / 4 * width
        self.rect_height = 1 / 2 * height

        # Adjust arrow coordinates and dimension according to the proporsions
        x, y = pos
        if direction == "right":  # Right arrow vertices
            self.pos = (x, 1 / 4 * height + y)
            self.top_vertices = [[x + width, 1 / 2 * height + y],
                                 [3 / 4 * width + x, y],
                                 [3 / 4 * width + x, y + height]]
            self.bottom_vertices = [[x + width, 1 / 2 * height + y],
                                    [3 / 4 * width + x, y],
                                    [3 / 4 * width + x, y + height]]
        else:  # Left arrow vertices
            self.pos = (1 / 4 * width + x, 1 / 4 * height + y)
            self.rect_width = 3 / 4 * width
            self.rect_height = 1 / 2 * height
            self.top_vertices = [[x, 1 / 2 * height + y],
                                 [1 / 4 * width + x, y],
                                 [1 / 4 * width + x, y + height]]
            self.bottom_vertices = [[x, 1 / 2 * height + y],
                                    [1 / 4 * width + x, y],
                                    [1 / 4 * width + x, y + height]]

        # Save original positions
        self.original_y_pos = self.pos[1]
        self.original_vetices = self.top_vertices

        # Top rectangle
        self.top_rect = pygame.Rect(self.pos, (self.rect_width, self.rect_height))
        self.TOP_COLOR = color
        self.top_color = color

        # Bottom rectangle
        self.bottom_rect = pygame.Rect(self.pos, (self.rect_width, self.rect_height))
        self.bottom_color = cfg.BLUE

        # Hitbox rectangle
        self.hitbox_rect = pygame.Rect(self.pos, (self.rect_width, self.rect_height))

        # Text
        gui_font = pygame.font.Font(cfg.chary_font, font_size)
        self.text_surf = gui_font.render(self.text, True, cfg.WHITE)
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)

    def draw(self, screen):
        """
        Draws the button
        :param screen:
        :return:
        """
        # Elevation logic
        self.top_rect.y = self.original_y_pos - self.dynamic_elevation
        self.text_rect.center = self.top_rect.center
        self.hitbox_rect.y = self.original_y_pos - self.elevation
        self.top_vertices = [[vertex[0], vertex[1] - self.dynamic_elevation] for vertex in self.original_vetices]

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation

        # Draw rect
        pygame.draw.rect(screen, self.bottom_color, self.bottom_rect)
        pygame.draw.rect(screen, self.top_color, self.top_rect)

        # Draw triangle
        pygame.draw.polygon(screen, self.bottom_color, self.bottom_vertices)
        pygame.draw.polygon(screen, self.top_color, self.top_vertices)

        screen.blit(self.text_surf, self.text_rect)
        self.check_click()

    def check_click(self):
        """
        Check for clicks and disable button when game is playing
        :return:
        """
        mouse_pos = pygame.mouse.get_pos()

        if cfg.whose_turn == "pc":
            self.disabled = True
        else:
            self.disabled = False

        if self.disabled:
            self.top_color = cfg.BROWN
            self.dynamic_elevation = 0
        elif self.hitbox_rect.collidepoint(mouse_pos):
            self.top_color = cfg.BROWN
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elevation = 0
                self.pressed = True
            else:
                if self.pressed:
                    self.dynamic_elevation = self.elevation
                    self.button_action()
                    self.pressed = False
        else:
            self.pressed = False
            self.dynamic_elevation = self.elevation
            self.top_color = self.TOP_COLOR

    def button_action(self):
        """
        Performs default button actions
        :return:
        """


class RightButton(ArrowButton):
    """ Right button moves the selected crumb to the right """

    def button_action(self):
        """
        Performs button actions
        :return:
        """
        if cfg.index < len(cfg.bit_string) - 2:
            cfg.index += 1


class LeftButton(ArrowButton):
    """ Left button moves the selected crumb to the left """

    def button_action(self):
        """
        Performs button actions
        :return:
        """
        if cfg.index > 0:
            cfg.index -= 1
