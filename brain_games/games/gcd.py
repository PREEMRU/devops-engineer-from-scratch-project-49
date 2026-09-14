from math import gcd
from random import randrange

DESC = "Find the greatest common divisor of given numbers."


def get_question_and_right_answer():
    n1 = randrange(0, 101)
    n2 = randrange(1, 101)
    numbers = f'{n1} {n2}'
    r_answer = gcd(n1, n2)
    return numbers, str(r_answer)
