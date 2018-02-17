def number_of_customers_per_state(customers_dict):
    results = {}
    for state, customers in customers_dict.items():
        if customers:
            results[state] = len(customers)
        else:
            results[state] = 0
    return results