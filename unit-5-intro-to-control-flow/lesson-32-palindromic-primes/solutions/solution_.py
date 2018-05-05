def reverse_str(s):
    return s[::-1]

def is_palindromic(n):
    return str(n) == reverse_str(str(n))

def is_prime(n):
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False

    i = 3
    while i < n-1:
        if n % i == 0:
            return False
        i += 2

    # Could have been written with a for-loop
    # for simplicity:
    #for i in range(3, n-1, 2):
    #    if n % i == 0:
    #        return False
    return True

def next_palindromic_prime(n):
    n += 1
    #while not is_palindromic(n) and not is_prime(n):
    while True:
        if is_palindromic(n) and is_prime(n):
            return n
        n += 1
