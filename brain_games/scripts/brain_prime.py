#!/usr/bin/env python3

import random
from brain_games.game_engine import play_game


def get_q_and_a():
    num = random.randint(0, 15)
    for i in range(2, num):
        if num % i == 0:
            return (str(num), 'no')
    return (str(num), 'yes')


def main():
    play_game(get_q_and_a, 3, 'Answer "yes" if given number is prime. Otherwise answer "no".')


if __name__ == main:
    main()
