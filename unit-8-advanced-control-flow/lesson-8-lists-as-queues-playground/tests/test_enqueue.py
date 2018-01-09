def test_enqueue():
    q = create_queue()

    enqueue(q, 'Ned Stark')
    assert q == ['Ned Stark']

    enqueue(q, 'Jon Snow')
    assert q == ['Ned Stark', 'Jon Snow']

    enqueue(q, 'Sansa Stark')
    enqueue(q, 'Robb Stark')

    assert q == ['Ned Stark', 'Jon Snow', 'Sansa Stark', 'Robb Stark']

