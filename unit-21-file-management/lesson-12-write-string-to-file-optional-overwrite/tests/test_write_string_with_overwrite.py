import tempfile

def test_write_string_with_overwrite():
    fp = tempfile.NamedTemporaryFile(mode="w")
    fp.write('this is line 1\n')
    fp.write('this is line 2\n')
    fp.write('this is line 3\n')
    fp.flush()
    
    write_string(fp.name, 'my name is john', overwrite_all=True)

    with open(fp.name) as fp:
        assert len(fp.readlines()) == 1
        fp.seek(0)
        assert f.readlines()[0] == 'my name is john\n'