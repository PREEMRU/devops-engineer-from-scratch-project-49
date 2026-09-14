import prompt

from brain_games.cli import welcome_user

ROUNDS_COUNT = 3


def engine(game):
    name = welcome_user()
    print(f"Hello, {name}!")
    print(game.DESC)

    for _ in range(ROUNDS_COUNT):
        question, correct_answer = game.get_question_and_right_answer()

        print(f"Question: {question}")
        answer = prompt.string("Your answer: ")

        if answer != correct_answer:
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

        print("Correct!")

    print(f"Congratulations, {name}!")