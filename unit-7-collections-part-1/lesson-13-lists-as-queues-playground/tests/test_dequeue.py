def test_dequeue():
    q = create_queue()

    enqueue(q, 'Ned Stark')
    enqueue(q, 'Jon Snow')
    enqueue(q, 'Sansa Stark')

    elem = dequeue(q)
    assert elem == 'Ned Stark'
    assert q == ['Jon Snow', 'Sansa Stark']

    elem = dequeue(q)
    assert elem == 'Jon Snow'
    assert q == ['Sansa Stark']

    elem = dequeue(q)
    assert elem == 'Sansa Stark'
    assert q == []

    # No more elements, returns None
    elem = dequeue(q)
    assert elem is None
    assert q == []

