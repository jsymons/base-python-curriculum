size_3_matrix = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
]

def test_size_3_identity_matrix():
    assert identity_matrix(3) == size_3_matrix
