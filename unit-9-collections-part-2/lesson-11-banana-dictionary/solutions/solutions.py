def banana_dict(num):
    bananas = {}
    for i in range(1, num + 1):
        bananas['banana' * i] = i
    return bananas
