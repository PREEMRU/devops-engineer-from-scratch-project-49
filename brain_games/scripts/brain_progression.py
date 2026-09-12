from random import randrange

from brain_games.scripts.engine import engine

DESC = "What number is missing in the progression?"


def progress():
    start = randrange(0, 101)
    step = randrange(1, 11)
    numbers = [start + step * i for i in range(10)]
    r_index = randrange(len(numbers))
    r_answer = numbers[r_index]
    numbers[r_index] = ".."
    question = ' '.join(map(str, numbers))
    return question, str(r_answer)


def main():
    engine(progress, DESC)


if __name__ == "__main__":
    main()