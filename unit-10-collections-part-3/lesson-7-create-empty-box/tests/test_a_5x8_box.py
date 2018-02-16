box_5x8_expected = """
xxxxxxxx
x      x
x      x
x      x
xxxxxxxx
""".lstrip()

def test_a_5x8_box():
    assert create_empty_box(5, 8, 'x') == box_5x8_expected
