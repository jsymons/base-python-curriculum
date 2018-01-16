def test_calculator_cache():
    c = Calculator()
    assert hasattr(c, 'cache')
    assert c.cache == {}

    assert c.add(2, 8) == 10
    assert c.cache == {
        'add': [
            (2, 8, 10)
        ]
    }

    assert c.subtract(7, 2) == 5
    assert c.cache == {
        'add': [
            (2, 8, 10)
        ],
        'subtract': [
            (7, 2, 5)
        ]
    }

    assert c.subtract(11, 7) == 4
    assert c.cache == {
        'add': [
            (2, 8, 10)
        ],
        'subtract': [
            (7, 2, 5),
            (11, 7, 4)
        ]
    }

    # Repeated operation. Should be cached
    assert c.add(2, 8) == 10
    assert c.cache == {
        'add': [
            (2, 8, 10)
        ],
        'subtract': [
            (7, 2, 5),
            (11, 7, 4)
        ]
    }
