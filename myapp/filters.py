


def price_filter(products,value):
    min_price = value.get('min_price')
    max_price = value.get('max_price')

    if min_price:
        products = products.filter(price__gte = min_price)

    if max_price:
        products = products.filter(price__lte = max_price)

    return products



def search(products,value):
    search = value.get('search')
    if search:
        products = products.filter(title__icontains = search)

    return products