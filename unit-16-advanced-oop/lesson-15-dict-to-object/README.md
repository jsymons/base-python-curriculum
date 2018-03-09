# Dict to Object

So perhaps you're starting to see the advantages of OOP. Sometimes you'll need to store dynamic data as attributes where you don't specifically know the attribute name ahead of time. Create a class `Commerical` that receives TV commericial information as a dictionary and stores the key-value info as attributes for the object.

This kind of trickery can be used to receive data from a JSON file and store it in an OOP format.

Example:

```python
tide_ad = Commercial({
                    "actor": "David Harbour",
                    "brand": "Tide",
                    "style": "Really weird",
                    "warning": "Don't eat Tide Pods"
})

tide_ad.actor # "David Harbour"
tide_ad.brand # "Tide"
tide_ad.style # "Really weird"
tide_ad.warning # "Don't eat Tide Pods"
```