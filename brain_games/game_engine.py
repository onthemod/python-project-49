import prompt


def greet():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def play_game(qa_function, attempts, task):
    name = greet()
    attempt = 0
    print(task)
    while attempt < attempts:
        qa = qa_function()
        question = qa[0]
        print(f'Question: {question}')
        user_ans = prompt.string('Your answer: ')
        correct_ans = qa[1]
        if user_ans != correct_ans:
            print(f"\'{user_ans}\' is wrong answer ;(. \
Correct answer was \'{correct_ans}\'.")
            print(f"Let\'s try again, {name}!")
            return
        print('Correct!')
        attempt = attempt + 1
    print(f"Congratulations, {name}!")
