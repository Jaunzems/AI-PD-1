""" Utility functions that can be used by all other files """
import pygame
from random import randint
import src.config as cfg


def computer_moves():
    """
    Computer makes a random move (runs every frame)
    :return:
    """
    if cfg.whose_turn == "pc" and cfg.game_state == "playing":
        current_time = pygame.time.get_ticks()

        # Initializes once with is_marked
        if not cfg.is_marked:
            cfg.last_time = current_time
            cfg.prev = 0
            if cfg.game_state == "playing":
                # Generate random index
                cfg.target_index = randint(0, len(cfg.bit_string) - 2)
            cfg.is_marked = True

        # Move selection box/index every 500 milliseconds
        if (current_time - cfg.last_time) // 500 != cfg.prev:
            if cfg.target_index != cfg.index:
                if cfg.target_index > cfg.index:
                    cfg.index += 1
                else:
                    cfg.index -= 1
            else:
                calculate(cfg.bit_string, cfg.target_index)
                cfg.whose_turn = "p1"

        # Sets a new prev time
        cfg.prev = (current_time - cfg.last_time) // 500
    else:
        cfg.is_marked = False


def generate_new_bit_string():
    """
    Generates a string of random 1s and 0s with difficulty as length
    :return:
    """
    bit_string = [str(randint(0, 1)) for _ in range(cfg.difficulty)]
    cfg.bit_string = "".join(bit_string)
    reset_index()


def calculate(bit_string, index):
    """
    Calculates the new bit_string and score
    :param bit_string:
    :param index:
    :return:
    """
    # Crumb. A group of two bits or a quarter byte is called a crumb
    crumb = bit_string[index] + bit_string[index + 1]

    # Calculates scores for each crumb combinations
    new_char = "-1"
    score = -1
    if crumb == "11":
        score = 2
        new_char = "1"
    elif crumb == "00":
        score = 2
        new_char = "0"
    elif crumb == "10":
        score = 1
        new_char = "1"
    elif crumb == "01":
        score = 1
        new_char = "0"

    # Replaces the two bits crumb with a one bit new_char
    new_string = ""
    for i, char in enumerate(bit_string):
        if i == index:
            new_string += new_char
        elif i == index + 1:
            continue
        else:
            new_string += char
    cfg.bit_string = new_string

    # Add the scores accordingly
    if cfg.whose_turn == "p1":
        cfg.p1_score += score
    elif cfg.whose_turn == "p2":
        cfg.p2_score += score
    else:
        cfg.pc_score += score

    reset_index()


def check_win_condition():
    """
    Checks win condition and index positioning
    :return:
    """
    if cfg.index > len(cfg.bit_string) - 2:
        cfg.index = len(cfg.bit_string) - 2
    if len(cfg.bit_string) == 2:
        cfg.index = 0
    if len(cfg.bit_string) == 1:
        cfg.game_state = "game_over"


def reset_index():
    """
    Reset's index position
    :return:
    """
    cfg.index = int(len(cfg.bit_string) / 2 - 1)


def reset_scores():
    """
    Resets all player's and computer's scores
    :return:
    """
    cfg.p1_score = 0
    cfg.p2_score = 0
    cfg.pc_score = 0
