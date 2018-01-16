def rmotr_zip(collection_a, collection_b):
    if len(collection_a) != len(collection_b):
        return None
    result = []

    for i in range(len(collection_a)):
        result.append((collection_a[i], collection_b[i]))

    return result
