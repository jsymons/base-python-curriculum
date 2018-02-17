def calculate_purchase_price(purchase, set_to_dict=False):
    total = 0
    books = purchase['books']
    for book in books:
        total += book['price']
    if set_to_dict:
        purchase['total'] = total
    return total