import random


def _get_random_number_not_repeated(previous_numbers):
    while True:
        number = random.randint(0, 100)
        if number not in previous_numbers:
            return number


def random_matrix(m, n):
    used_numbers = []
    matrix = []

    for i in range(m):
        row = []
        for j in range(n):
            number = _get_random_number_not_repeated(used_numbers)
            row.append(number)
            used_numbers.append(number)
        matrix.append(row)

    return matrix
