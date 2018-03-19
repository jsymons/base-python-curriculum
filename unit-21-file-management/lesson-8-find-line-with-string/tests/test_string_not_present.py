import tempfile

def test_string_not_present():
    fp = tempfile.NamedTemporaryFile(mode="w")
    fp.write('this is line 1\n')
    fp.write('this is line 2\n')
    fp.write('this is line 3\n')
    fp.flush()

    assert which_line(fp.name, 'foobar') == None

    fp.close()