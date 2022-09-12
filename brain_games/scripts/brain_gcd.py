#!/usr/bin/env python3

import random
from brain_games.game_engine import play_game


def get_q_and_a():
    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)
    ans = 1
    if num1 < num2:
        for i in range(num1):
            if num2 % (i + 1) == 0 and num1 % (i + 1) == 0:
                ans = i + 1
    else:
        for i in range(num2):
            if num2 % (i + 1) == 0 and num1 % (i + 1) == 0:
                ans = i + 1
    return (f'{num1} {num2}', str(ans))


def main():
    play_game(get_q_and_a, 3,
              "Find the greatest common divisor of given numbers.")


if __name__ == main:
    main()
