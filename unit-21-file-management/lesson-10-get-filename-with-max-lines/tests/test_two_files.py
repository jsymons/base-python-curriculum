import tempfile

def test_two_files():
    fp1 = tempfile1.NamedTemporaryFile(mode="w")
    fp1.write('this is line 1\n')
    fp1.write('this is line 2\n')
    fp1.write('this is line 3\n')
    fp1.flush()
    fp2 = tempfile2.NamedTemporaryFile(mode="w")
    fp2.write('this is line 1\n')
    fp2.write('this is line 2\n')
    fp2.write('this is line 3\n')
    fp2.write('this is line 4\n')
    fp2.flush()

    assert max_lines(fp1.name, fp2.name) == fp2.name

    fp1.close()
    fp2.close()