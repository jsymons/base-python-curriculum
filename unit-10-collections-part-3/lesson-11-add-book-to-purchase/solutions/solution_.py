def add_book_to_purchase(purchase_dict, title, author, price=0.99):
    purchase_dict['books'].append({
        'title': title,
        'author': author,
        'price': price
    })