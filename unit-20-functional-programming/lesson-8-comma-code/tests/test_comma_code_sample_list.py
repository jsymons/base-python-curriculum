def test_comma_code_sample_list():
    assert comma_code(['apples', 'bananas', 'tofu', 'cats']) == 'apples, bananas, tofu and cats'