def test_factorial_terms_are_generated_ok():
    """Should return the correct terms for a number"""
    assert factorial_terms(5) == [5, 4, 3, 2, 1]