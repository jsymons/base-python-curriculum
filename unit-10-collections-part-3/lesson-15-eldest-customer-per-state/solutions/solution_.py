def eldest_customer_per_state(customers_dict):
    results = {}
    for state, customers in customers_dict.items():
        eldest_customer = None
        for customer in customers:
            if eldest_customer is None or customer['age'] > eldest_customer['age']:
                eldest_customer = customer
        results[state] = eldest_customer

    return results