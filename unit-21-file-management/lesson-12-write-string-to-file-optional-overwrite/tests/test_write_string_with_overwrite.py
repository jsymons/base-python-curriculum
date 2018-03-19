import tempfile

def test_write_string_with_overwrite():
    fp = tempfile.NamedTemporaryFile(mode="w")
    fp.write('this is line 1\n')
    fp.write('this is line 2\n')
    fp.write('this is line 3\n')
    fp.flush()

    assert read_first_line(fp.name) == 'this is line 1\n'

    fp.close()