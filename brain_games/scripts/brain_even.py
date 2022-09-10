#!/usr/bin/env python3

import random
from brain_games.game_engine import play_game


def get_q_and_a():
    num = random.randint(0, 100)
    ans = 'yes' if num % 2 == 0 else 'no'
    return (num, ans)


def main():
    play_game(get_q_and_a, 3, 'Answer "yes" if the number is even, otherwise answer "no".')


if __name__ == main:
    main()
