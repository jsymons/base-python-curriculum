def test_asc_order():
    fp = tempfile.NamedTemporaryFile(mode="w")
    fp.write('line 3\n')
    fp.write('line 1\n')
    fp.write('line 2\n')
    fp.write('line 4\n')
    fp.flush()
    
    sort_lines(fp.name)

    with open(fp.name) as fp:
        assert fp.readlines()[0] == 'line 1\n'
        fp.seek(0)
        assert fp.readlines()[1] == 'line 2\n'
