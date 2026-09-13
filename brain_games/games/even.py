from random import randrange

DESC = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even():
    numbers = randrange(0, 101)
    r_answer = 'yes' if numbers % 2 == 0 else 'no'
    return numbers, r_answer
