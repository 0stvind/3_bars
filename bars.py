import json

def load_data(filepath):
    with open(filepath, 'r') as file_handler:
        bars = json.load(file_handler)
    bars_info = dict()
    for bar_number,bar in enumerate(bars):      
        bars_info[bars[bar_number]['Cells']['Name']] = [bars[bar_number]['Cells']['geoData']['coordinates'] , bars[bar_number]['Cells']['SeatsCount']]
    return bars_info

def get_biggest_bar(data):
    bars = data
    max_number = 0
    biggest = ''
    for bar_name in bars:
      if(bars[bar_name][1] > max_number):
        biggest = bar_name
        max_number = bars[bar_name][1]
    return biggest


def get_smallest_bar(data):
    bars = data
    min_number = 1000000
    smallest = ''
    for bar_name in bars:    
      if(bars[bar_name][1] < min_number):
        smallest = bar_name
    return smallest


def get_closest_bar(data, longitude, latitude):
    bars = data
    min_difference = 1000000
    closest = ''
    for bar_name in bars:
      if(abs((longitude + latitude) - bars[bar_name][0][0] + bars[bar_name][0][1]) < min_difference):
        closest = bar_name
        min_difference = abs((longitude + latitude) - bars[bar_name][0][0] + bars[bar_name][0][1])
    return closest
if __name__ == '__main__':
    load_data('bars.json')
    biggest = get_biggest_bar(load_data('bars.json'))
    smallest = get_smallest_bar(load_data('bars.json'))
    closest = get_closest_bar(load_data('bars.json'), 35, 48)
    print('The biggest bar is %s. The smallest bar is %s. The closest bar is %s' % (biggest, smallest, closest))
