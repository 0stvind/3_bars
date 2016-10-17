import json


def load_data(filepath):
    with open(filepath, 'r') as file_handler:
        bars = json.load(file_handler)
    return bars


def g(bar, val1):
    if val1 is None:
        return bar['Cells']['SeatsCount']
    elif val1 == 'N':
        return bar['Cells']['Name']
    else:
        return bar['Cells']['geoData']['coordinates'][val1]


def get_biggest_bar(data):
    b = max(data, key=lambda bar: g(bar, None))
    return g(b, 'N')


def get_smallest_bar(data):
    s = min(data, key=lambda bar: g(bar, None))
    return g(s, 'N')


def get_closest_bar(data, lon, lat):
    close = min(data, key=lambda bar: abs(lon - g(bar, 0) + lat - g(bar, 1)))
    return g(close, 'N')


if __name__ == '__main__':
    filepath = input('Введите путь до файла ')
    longitude = float(input('Введите вашу долготу '))
    latitude = float(input('Введите вашу широту '))
    load = load_data(filepath)
print("The biggest bar is %s. The smallest bar is %s."
      "The closest bar is %s" % (get_biggest_bar(load),
                                 get_smallest_bar(load),
                                 get_closest_bar(load, longitude, latitude)))
