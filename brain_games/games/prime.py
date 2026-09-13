from random import randrange

DESC = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime():
    numbers = randrange(0, 101)
    prime = True

    if numbers < 2:
        prime = False
    else:
        for i in range(2, int(numbers ** 0.5) + 1):
            if numbers % i == 0:
                prime = False
                break

    r_answer = 'yes' if prime else 'no'
    return numbers, r_answer
