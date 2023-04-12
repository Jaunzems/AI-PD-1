""" Button class file """
import pygame
import src.config as cfg
import src.util as util


class Button:
    """ Button abstract class """

    def __init__(self, text, width, height, pos, color, font_size=20):
        # Core attributes
        self.pressed = False
        self.disabled = False
        self.elevation = 4
        self.dynamic_elevation = self.elevation
        self.original_y_pos = pos[1]
        self.text = text
        self.pos = pos
        self.font_size = font_size

        # Top rectangle
        self.top_rect = pygame.Rect(pos, (width, height))
        self.TOP_COLOR = color
        self.top_color = color

        # Bottom rectangle
        self.bottom_rect = pygame.Rect(pos, (width, height))
        self.bottom_color = cfg.BLUE

        # Hitbox rectangle
        self.hitbox_rect = pygame.Rect(pos, (width, height))

        # Text
        self.gui_font = pygame.font.Font(cfg.chary_font, self.font_size)
        self.text_surf = self.gui_font.render(self.text, True, cfg.WHITE)
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)

    def draw(self, screen):
        """
        Draws the button
        :param screen:
        :return:
        """
        self.check_click()
        self.update()

        # elevation logic
        self.top_rect.y = self.original_y_pos - self.dynamic_elevation
        self.text_rect.center = self.top_rect.center
        self.hitbox_rect.y = self.original_y_pos - self.elevation

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation

        pygame.draw.rect(screen, self.bottom_color, self.bottom_rect, border_radius=5)
        pygame.draw.rect(screen, self.top_color, self.top_rect, border_radius=5)

        screen.blit(self.text_surf, self.text_rect)

    def check_click(self):
        """
        Check if the button is clicked
        :return:
        """
        mouse_pos = pygame.mouse.get_pos()

        if self.hitbox_rect.collidepoint(mouse_pos):
            self.top_color = cfg.BROWN
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elevation = 0
                self.pressed = True
            else:
                self.dynamic_elevation = self.elevation
                if self.pressed:
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

    def update(self):
        """
        Optional updates for subclasses
        :return:
        """


class SelectButton(Button):
    """ Select button that selects which bits are going to be calculated """

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
        Performs button actions
        :return:
        """
        if len(cfg.bit_string) > 1:
            cfg.game_state = "playing"
        if len(cfg.bit_string) > 1:
            util.calculate(cfg.bit_string, cfg.index)
            if cfg.whose_turn == "p1":
                if cfg.opponent == "player":
                    cfg.whose_turn = "p2"
                else:
                    cfg.whose_turn = "pc"
            else:
                cfg.whose_turn = "p1"

    def update(self):
        """
        Updates button color according to whose turn is it to play
        :return:
        """
        if cfg.whose_turn == "p2":
            self.TOP_COLOR = cfg.GREEN
        else:
            self.TOP_COLOR = cfg.RED


class RestartButton(Button):
    """ Restarts the game """

    def button_action(self):
        """
        Performs button actions
        :return:
        """
        if cfg.whose_turn == "pc":
            cfg.game_state = "playing"
            if len(cfg.bit_string) < 2:
                util.generate_new_bit_string()
                util.reset_index()
                util.reset_scores()

                if cfg.whose_first == "computer":
                    cfg.whose_turn = "pc"
                else:
                    cfg.whose_turn = "p1"

                cfg.game_state = "game_over"
        else:
            util.generate_new_bit_string()
            util.reset_index()
            util.reset_scores()

            if cfg.whose_first == "computer" and cfg.opponent == "computer":
                cfg.whose_turn = "pc"
            else:
                cfg.whose_turn = "p1"
            cfg.game_state = "game_over"

    def update(self):
        """
        Updates the button's text
        :return:
        """
        if cfg.game_state == "playing" or len(cfg.bit_string) < 2:
            text = "Restart"
        else:
            text = "Start"
        self.text_surf = self.gui_font.render(text, True, cfg.WHITE)
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)


class DifficultyToggleButton(Button):
    """ Toggles difficulty between Easy, Medium, and Hard """

    def check_click(self):
        """
        Check for clicks and disable button when game is playing
        :return:
        """
        mouse_pos = pygame.mouse.get_pos()

        if cfg.game_state == "playing":
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
        Performs button actions
        :return:
        """
        # Cycles through the difficulty list and updates the index inside the list
        cfg.difficulty = cfg.difficulty_list[1][cfg.difficulty_list[0]]
        cfg.difficulty_list[0] = (cfg.difficulty_list[0] + 1) % len(cfg.difficulty_list[1])

        # Text update logic
        text = ""
        if cfg.difficulty == cfg.EASY:
            text = "Easy"
            self.TOP_COLOR = cfg.GREEN
        elif cfg.difficulty == cfg.MEDIUM:
            text = "Medium"
            self.TOP_COLOR = cfg.YELLOW
        elif cfg.difficulty == cfg.HARD:
            text = "Hard"
            self.TOP_COLOR = cfg.RED

        # Updates text rect
        self.gui_font = pygame.font.Font(cfg.chary_font, self.font_size)
        self.text_surf = self.gui_font.render(text, True, cfg.WHITE)
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)

        # Util functions
        util.generate_new_bit_string()
        util.reset_scores()


class OpponentToggleButton(Button):
    """ Toggles between player and computer opponents """

    def check_click(self):
        """
        Check for clicks and disable button when game is playing
        :return:
        """
        mouse_pos = pygame.mouse.get_pos()

        if cfg.game_state == "playing":
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
        Performs button actions
        :return:
        """
        util.reset_scores()

        # Cycles through the opponent list and updates the index inside the list
        cfg.opponent = cfg.opponent_list[1][cfg.opponent_list[0]]
        cfg.opponent_list[0] = (cfg.opponent_list[0] + 1) % len(cfg.opponent_list[1])

        # Whose turn logic
        if cfg.opponent == "player":
            cfg.whose_turn = "p1"
        else:
            if cfg.whose_first == "player":
                cfg.whose_turn = "p1"
            else:
                cfg.whose_turn = "pc"

        # Text update logic
        new_text = ""
        if cfg.opponent == "player":
            new_text = "Player"
            self.TOP_COLOR = cfg.GREEN
        elif cfg.opponent == "computer":
            new_text = "Computer"
            self.TOP_COLOR = cfg.YELLOW

        # Updates text rect
        self.gui_font = pygame.font.Font(cfg.chary_font, self.font_size)
        self.text_surf = self.gui_font.render(new_text, True, cfg.WHITE)
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)


class WhoseFirstButton(Button):
    """ Toggles between who goes first in a Player vs Computer match """

    def check_click(self):
        """
        Check for clicks and disable button when game is playing
        :return:
        """
        mouse_pos = pygame.mouse.get_pos()

        if cfg.game_state == "playing" or cfg.opponent == "player":
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
        Performs button actions
        :return:
        """
        # Cycles between player and computer on who goes first
        if cfg.whose_first == "player":
            cfg.whose_first = "computer"
            cfg.whose_turn = "pc"
            new_text = "Computer First"
            self.TOP_COLOR = cfg.YELLOW
        else:
            cfg.whose_first = "player"
            cfg.whose_turn = "p1"
            new_text = "Player First"
            self.TOP_COLOR = cfg.RED

        # Updates text rect
        self.gui_font = pygame.font.Font(cfg.chary_font, self.font_size)
        self.text_surf = self.gui_font.render(new_text, True, cfg.WHITE)
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)
