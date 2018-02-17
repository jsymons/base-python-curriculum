desc_pyramid = """
xxxxxxx
xxxxxx
xxxxx
xxxx
xxx
xx
x
""".lstrip()


def test_descending_pyramid():
    assert advanced_nested_pyramid(7, 'x', 'DESC') == desc_pyramid
