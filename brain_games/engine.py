import prompt

from brain_games.cli import welcome_user


def engine(func, desc):
    name = welcome_user()
    print(f'Hello, {name}!')

    print(desc)

    for i in range(3):
        question, r_answer = func()

        print(f"Question: {question}")
        answer = prompt.string("Your answer: ")

        if answer == r_answer:
            print("Correct!")
            if i == 2:
                print(f"Congratulations, {name}!")
        else:
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{r_answer}'."
            )
            print(f"Let's try again, {name}!")
            break