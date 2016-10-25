import json


def load_data(filepath):
    with open(filepath, 'r') as file_handler:
        bars = json.load(file_handler)
    return bars


def get_value(bar, val):
    if val == 'Seats':
        return bar['Cells']['SeatsCount']
    elif val == 'Name':
        return bar['Cells']['Name']
    else:
        return bar['Cells']['geoData']['coordinates'][val]


def get_biggest_bar(data):
    biggest = max(data, key=lambda bar: get_value(bar, 'Seats'))
    return get_value(biggest, 'Name')


def get_smallest_bar(data):
    smallest = min(data, key=lambda bar: get_value(bar, 'Seats'))
    return get_value(smallest, 'Name')


def get_closest_bar(data, longitude, latitude):
    closest = min(data, key=lambda bar: abs(longitude - get_value(bar, 0) + \
                                            latitude - get_value(bar, 1)))
    return get_value(closest, 'Name')


if __name__ == '__main__':
    filepath = input('Введите путь до файла ')
    longitude = float(input('Введите вашу долготу '))
    latitude = float(input('Введите вашу широту '))
    data = load_data(filepath)
print("The biggest bar is %s. The smallest bar is %s."
      "The closest bar is %s" % (get_biggest_bar(data),
                                 get_smallest_bar(data),
                                 get_closest_bar(data, longitude, latitude)))
