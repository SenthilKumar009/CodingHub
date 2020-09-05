matches = {'Bread': 'bag', 'Milk': 'bottle', 'Eggs': 'carton', 'Cereals': 'box', 'Candy': 'plastic'}
#matches = {}

def get_container(product):
    if not bool(matches):
        return True
    elif product in matches:
        return matches[product]
    else:
        return 'Product is not available!'

print(get_container('Choco'))