import tempfile

def test_write_lines_to_file():
    fp = tempfile.NamedTemporaryFile(mode="w")
    write_lines((fp.name), ['my', 'name', 'is', 'john'])
    # fp.flush()
    with open(fp.name) as fp:
        assert len(fp.readlines()) == 4
        fp.seek(0)
        assert fp.readlines()[2] == 'is\n'