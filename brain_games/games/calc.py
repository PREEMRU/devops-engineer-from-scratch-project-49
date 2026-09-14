import operator
from random import choice, randint

DESC = "What is the result of the expression?"

MIN_NUMBER = 0
MAX_NUMBER = 100

OPERATIONS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
}


def get_question_and_right_answer():
    first_number = randint(MIN_NUMBER, MAX_NUMBER)
    second_number = randint(MIN_NUMBER, MAX_NUMBER)
    operation = choice(tuple(OPERATIONS))

    question = f"{first_number} {operation} {second_number}"
    correct_answer = OPERATIONS[operation](first_number, second_number)

    return question, str(correct_answer)