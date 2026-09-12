from math import gcd
from random import randrange

from brain_games.scripts.engine import engine

DESC = "Find the greatest common divisor of given numbers."


def gcdd():
    n1 = randrange(0, 101)
    n2 = randrange(1, 101)
    numbers = f'{n1} {n2}'
    r_answer = gcd(n1, n2)
    return numbers, str(r_answer)


def main():
    engine(gcdd, DESC)


if __name__ == "__main__":
    main()