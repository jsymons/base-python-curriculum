box_3x4_expected = """
****
****
****
""".lstrip()

def test_a_3x4_box():
    assert create_box(3, 4, '*') == box_3x4_expected
