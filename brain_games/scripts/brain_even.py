import prompt
import random


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    attempt = 0
    while attempt < 3:
        num = random.randint(0, 100)
        print(f'Question: {str(num)}')
        ans = prompt.string('Your answer: ')
        ra = 'yes'
        if num % 2 == 1:
            ra = 'no'
        if ans != ra:
            print(f"\'{ans}\' is wrong answer ;(. Correct answer was \'{ra}\'.")
            print(f"Let\'s try again, {name}!")
            return
        print('Correct!')
        attempt = attempt + 1
    print(f"Congratulations, {name}!")


if __name__ == main:
    main()
