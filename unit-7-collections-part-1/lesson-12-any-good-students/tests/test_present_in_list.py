def test_present_in_list():
    assert check_for_good_student(['bad_student', 'good_student', 'decent_student']) == True
