from random import randrange

from brain_games.scripts.engine import engine

DESC = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even():
    numbers = randrange(0, 101)
    r_answer = 'yes' if numbers % 2 == 0 else 'no'
    return numbers, r_answer


def main():
    engine(is_even, DESC)


if __name__ == "__main__":
    main()