def test_next_palindromic_primes():
    assert next_palindromic_prime(100) == 101
    assert next_palindromic_prime(150) == 151
    assert next_palindromic_prime(160) == 181
    assert next_palindromic_prime(200) == 313
    assert next_palindromic_prime(10000) == 10301
    assert next_palindromic_prime(12000) == 12421
