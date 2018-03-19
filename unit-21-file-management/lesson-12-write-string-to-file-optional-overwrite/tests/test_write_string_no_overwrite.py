import tempfile

def test_write_string_no_overwrite():
    fp = tempfile.NamedTemporaryFile(mode="w")
    fp.write('this is line 1\n')
    fp.write('this is line 2\n')
    fp.write('this is line 3\n')
    fp.flush()
    
    write_string(fp.name, 'my name is john')

    with open(fp.name) as fp:
        assert len(fp.readlines()) == 4
        fp.seek(0)
        assert fp.readlines()[3] == 'my name is john\n'