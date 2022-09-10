#!/usr/bin/env python3

import random
from brain_games.game_engine import play_game


def get_q_and_a():
    length = random.randint(5, 15)
    num = random.randint(0, length)
    start = random.randint(0, 100)
    step = random.randint(1, 10)
    s = ''
    ans = start
    for i in range(length):
        if i != num:
            s = s + str(start) + ' '
        else:
            s = s + '.. '
            ans = start
        start = start + step
    return (s, str(ans))


def main():
    play_game(get_q_and_a)


if __name__ == main:
    main()
