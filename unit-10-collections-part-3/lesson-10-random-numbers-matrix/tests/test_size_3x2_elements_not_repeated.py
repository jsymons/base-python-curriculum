def test_size_3x2_elements_not_repeated():
    matrix = random_matrix(3, 2)

    assert len(matrix) == 3
    for row in matrix:
        assert len(row) == 2

    repeated_elements = []
    for row in matrix:
        for elem in row:
            assert elem not in repeated_elements
            repeated_elements.append(elem)

