#!/usr/bin/env python3

import random
from brain_games.game_engine import play_game


def get_q_and_a():
    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)
    act = random.randint(0, 2)
    if act == 0:
        return (f'{num1} + {num2}', str(num1 + num2))
    elif act == 1:
        return (f'{num1} - {num2}', str(num1 - num2))
    else:
        return (f'{num1} * {num2}', str(num1 * num2))


def main():
    play_game(get_q_and_a)


if __name__ == main:
    main()
