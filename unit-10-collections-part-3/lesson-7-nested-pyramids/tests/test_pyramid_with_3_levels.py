pyramid_3_expected = """
@
@@
@@@
""".lstrip()


def test_pyramid_with_3_levels():
    assert nested_pyramid(3, '@') == pyramid_3_expected
