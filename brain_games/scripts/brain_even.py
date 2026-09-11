from random import randrange

import prompt

from brain_games.cli import welcome_user


def is_even():
    number = randrange(0, 100)
    if number % 2 == 0:
        even = "yes"
    else:
        even = "no"
    return number, even


def main():
    name = welcome_user()
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')

    for i in range(3):
        number, even = is_even()

        print(f"Question: {number}")
        answer = prompt.string("Your answer: ")

        if answer == even:
            print("Correct!")
            if i == 2:
                print(f"Congratulations, {name}!")
        else:
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{even}'."
            )
            print(f"Let's try again, {name}!")
            break


if __name__ == "__main__":
    main()