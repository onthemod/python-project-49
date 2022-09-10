import prompt
import random


def get_q_and_a():
    num = random.randint(0, 100)
    ans = 'yes' if num % 2 == 0 else 'no'
    return (num, ans)


def greet():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    return name


def play_game():
    name = greet()
    attempt = 0
    while attempt < 3:
        qa = get_q_and_a()
        ra = qa[0]
        print(f'Question: {qa[0]}')
        ans = prompt.string('Your answer: ')
        ra = qa[1]
        if ans != ra:
            print(f"\'{ans}\' is wrong answer ;(. Correct answer was \'{ra}\'.")
            print(f"Let\'s try again, {name}!")
            return
        print('Correct!')
        attempt = attempt + 1
    print(f"Congratulations, {name}!")


def main():
    play_game()


if __name__ == main:
    main()
