import json


def load_data(filepath):
    with open(filepath, 'r') as file_handler:
        bars = json.load(file_handler)
    return bars


def get_biggest_bar(data):
    bars = data
    biggest = max(bars, key=lambda bar: bar['Cells']['SeatsCount'])
    return biggest['Cells']['Name']


def get_smallest_bar(data):
    bars = data
    smallest = min(bars, key=lambda bar: bar['Cells']['SeatsCount'])
    return smallest['Cells']['Name']


def get_closest_bar(data, longitude, latitude):
    bars = data
    closest = min(bars, key=lambda \
                  bar:abs(longitude - \
                  bar['Cells']['geoData']['coordinates'][0]) + \
                  latitude - bar['Cells']['geoData']['coordinates'][1])
    return closest['Cells']['Name']
if __name__ == '__main__':
    filepath = input('Введите путь до файла ')
    longitude = float(input('Введите вашу долготу '))
    latitude = float(input('Введите вашу широту '))
    load_data(filepath)
    biggest = get_biggest_bar(load_data(filepath))
    smallest = get_smallest_bar(load_data(filepath))
    closest = get_closest_bar(load_data(filepath), longitude, latitude)
print("The biggest bar is %s. The smallest bar is %s."
      "The closest bar is %s" % (biggest, smallest, closest))
