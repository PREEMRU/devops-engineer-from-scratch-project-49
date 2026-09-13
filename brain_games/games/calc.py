from random import choice, randrange

DESC = "What is the result of the expression?"


def calc():
    n1 = randrange(0, 101)
    n2 = randrange(0, 101)
    do = choice(['+', '-', '*'])
    numbers = f"{n1} {do} {n2}"
    r_answer = eval(numbers)
    return numbers, str(r_answer)
