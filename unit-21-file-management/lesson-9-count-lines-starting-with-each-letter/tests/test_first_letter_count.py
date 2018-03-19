import tempfile

def test_first_letter_count():
    fp = tempfile.NamedTemporaryFile(mode="w")
    fp.write('tree\n')
    fp.write('car\n')
    fp.write('car\n')
    fp.write('house\n')
    fp.flush()

    counter = counter_by_letter(fp.name)
    assert len(counter.keys()) == 26
    assert counter['c'] == 2
    assert counter['t'] == 1
    assert counter['h'] == 1
    assert counter['m'] == 0

    fp.close()