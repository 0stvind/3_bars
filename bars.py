import json


def load_data(filepath):
    with open(filepath, 'r') as file_handler:
        bars = json.load(file_handler)
    bars_info = []
    for bar_number, bar in enumerate(bars):
        temp = {'Name': bars[bar_number]['Cells']['Name'],
                'Seats': bars[bar_number]['Cells']['SeatsCount'],
                'coordinates':
                bars[bar_number]['Cells']['geoData']['coordinates']}
        bars_info.append(temp)
    return bars_info


def get_biggest_bar(data):
    bars = data
    biggest = max(bars, key=lambda bar: bar['Seats'])
    return biggest['Name']


def get_smallest_bar(data):
    bars = data
    smallest = min(bars, key=lambda bar: bar['Seats'])
    return smallest['Name']


def get_closest_bar(data, longitude, latitude):
    bars = data
    min_diff = 1000000
    closest = ''
    for bar_number, bar in enumerate(bars):
        if(abs((longitude + latitude) - bars[bar_number]['coordinates'][0] +
               bars[bar_number]['coordinates'][1]) < min_diff):
            closest = bars[bar_number]['Name']
            longitude1 = bars[bar_number]['coordinates'][0]
            latitude1 = bars[bar_number]['coordinates'][1]
            bars[bar_number]['coordinates'][1]
            min_diff = abs(longitude - longitude1) + abs(latitude - latitude1)
    return closest
if __name__ == '__main__':
    print('Введите путь до файла ')
    filepath = input()
    print('Введите вашу долготу')
    longitude = float(input())
    print('Введите вашу широту')
    latitude = float(input())
    load_data(filepath)
    biggest = get_biggest_bar(load_data(filepath))
    smallest = get_smallest_bar(load_data(filepath))
    closest = get_closest_bar(load_data(filepath), longitude, latitude)
print("The biggest bar is %s. The smallest bar is %s."
      "The closest bar is %s" % (biggest, smallest, closest))
