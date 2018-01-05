def test_push():
    s = create_stack()

    push(s, 'Ned Stark')
    assert s == ['Ned Stark']

    push(s, 'Jon Snow')
    assert s == ['Jon Snow', 'Ned Stark']

    push(s, 'Sansa Stark')
    push(s, 'Robb Stark')

    assert s == ['Robb Stark', 'Sansa Stark', 'Jon Snow', 'Ned Stark']
