def test_house_search():
    house = Location({
        'dresser': 'socks',
        'pantry': 'cake',
        'safe': 'money'
    })

    assert house.search(['basement', 'closet', 'bed', 'dresser']) == ['socks'] 