def test_object_is_created():
    s = SimpleClass()
    assert isinstance(s, SimpleClass) is True
    assert isinstance(s, object)
