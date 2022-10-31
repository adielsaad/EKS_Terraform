import requests
import json
import os


def get_lat_lon(input_location, API_key):
    url = f'http://api.openweathermap.org/geo/1.0/direct?q={input_location}&limit=5&appid={API_key}'
    data = requests.get(url).json()
    lat = str(data[0]['lat'])
    lon = str(data[0]['lon'])
    return get_data(lat, lon, API_key)


def get_data(lat, lon, API_key):
    second_url = f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=hourly,minutely&units=metric&appid={API_key}'
    data_dict = requests.get(second_url).json()
    print(data_dict)
    logic_data_dict = {}
    for i in range(0, 7):
        logic_data_dict[i] = { "min": data_dict['daily'][i]['temp']['min'],
                                "max": data_dict['daily'][i]['temp']['max'],
                                "night":  data_dict['daily'][i]['temp']['night'],
                                "humidity":  data_dict['daily'][i]['humidity']
                               }
    return logic_data_dict


def appendHistory(input, today_date, current_time):
    dict = {'date': today_date, 'time': str(current_time), 'city': input}
    isExist = os.path.exists("history.json")
    if isExist is False:
        with open("history.json", "w") as history_file:
            json.dump([dict], history_file)
    else:
        with open("history.json", "r") as history_file:
            feeds = json.load(history_file)
            feeds.append(dict)
        with open("history.json", 'w') as history_file:
            history_file.write(json.dumps(feeds, indent=4))


if __name__ == "__main__":
    None
