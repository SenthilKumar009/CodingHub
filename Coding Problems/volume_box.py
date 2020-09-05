measurement = {'height': 12, 'length': 14, 'width':20}

def volume(measurement):
    return measurement['height'] * measurement['width'] * measurement['length']

print('Volume:', volume(measurement))