def test_not_present_in_list():
    assert check_for_good_student(['bad_student', 'terrible_student', 'Santiago']) == False
