import tempfile

def test_one_file():
    fp = tempfile.NamedTemporaryFile(mode="w")
    fp.write('this is line 1\n')
    fp.write('this is line 2\n')
    fp.write('this is line 3\n')
    fp.flush()

    assert max_lines(fp.name) == fp.name

    fp.close()
