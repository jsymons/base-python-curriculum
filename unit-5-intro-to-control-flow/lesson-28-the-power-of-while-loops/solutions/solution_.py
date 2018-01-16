def feel_the_power(initial_number, power):
    result = 1
    power_count = 0
    while power_count < power:
        result *= initial_number
        power_count += 1
    return result