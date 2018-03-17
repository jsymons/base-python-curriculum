def factorial_terms(a_number):
    if a_number < 0:
        raise ValueError("Only defined for positive numbers")
    return list(range(a_number or 1, 0, -1))


def compute_factorial(terms):
    if not terms:
        raise ValueError("Terms should have at least one element")
    return reduce(lambda a, b: a*b, terms, 1)


def factorial(number):
    return compute_factorial(factorial_terms(number))