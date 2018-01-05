def test_pop():
    s = create_stack()

    push(s, 'Ned Stark')
    push(s, 'Jon Snow')
    push(s, 'Sansa Stark')
    push(s, 'Robb Stark')

    elem = pop(s)
    assert elem == 'Robb Stark'

    elem = pop(s)
    assert elem == 'Sansa Stark'

    elem = pop(s)
    assert elem == 'Jon Snow'

    elem = pop(s)
    assert elem == 'Ned Stark'

    # Empty stack
    elem = pop(s)
    assert elem == None
