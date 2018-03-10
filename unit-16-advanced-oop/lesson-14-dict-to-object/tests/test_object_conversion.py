def test_object_conversion():
    tide_ad = Commercial({
                    "actor": "David Harbour",
                    "brand": "Tide",
                    "style": "Really weird",
                    "warning": "Don't eat Tide Pods"
    })

    assert tide_ad.actor == "David Harbour"
    assert tide_ad.brand == "Tide"
    assert tide_ad.style == "Really weird"
    assert tide_ad.warning == "Don't eat Tide Pods"