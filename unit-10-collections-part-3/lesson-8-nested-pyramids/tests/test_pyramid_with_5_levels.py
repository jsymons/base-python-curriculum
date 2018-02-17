pyramid_5_expected = """
#
##
###
####
#####
""".lstrip()


def test_pyramid_with_5_levels():
    assert nested_pyramid(5, '#') == pyramid_5_expected
