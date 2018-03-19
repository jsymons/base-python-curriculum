import tempfile

def test_copy_file():
    fp1 = tempfile.NamedTemporaryFile(mode="w")
    fp1.write('this is line 1\n')
    fp1.write('this is line 2\n')
    fp1.write('this is line 3\n')
    fp1.flush()
    fp2 = tempfile.NamedTemporaryFile(mode="w")
    
    copy_file(fp1.name, fp2.name)

    fp1.close()

    with open(fp2.name) as fp2:
        assert len(fp2.readlines()) == 3
        fp2.seek(0)
        assert fp2.readlines()[2] == 'this is line 3\n'