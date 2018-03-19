import tempfile

def test_read_last_line():
    fp = tempfile.NamedTemporaryFile(mode="w")
    fp.write('this is line 1\n')
    fp.write('this is line 2\n')
    fp.write('this is line 3\n')
    fp.flush()

    assert read_line_number(fp.name, 3) == 'this is line 3\n'

    fp.close()