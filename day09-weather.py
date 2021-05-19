'''
Function:       Show Weather of entered zip code
Date:           02.09.2019
Created By:     Anonymous Systems
Dependencies:   requests, zipcodes, API KEY
'''
from requests import get
import zipcodes
import sys
import json


class Application:
    key = '5ad92f06b325ea17' # API Key
    if len(sys.argv) > 1:
        if zipcodes.is_real(sys.argv[1]):
            zip = sys.argv[1]
    else:
        zip = input('For which ZIP code would you like to see the weather? ')
    url = 'http://api.wunderground.com/api/' + key + '/geolookup/conditions/q/PA/' + zip + '.json'
    f = get(url)
    json_string = f.content
    parsed_json = json.loads(json_string)
    citystate = parsed_json['current_observation']['display_location']['full']
    weather = parsed_json['current_observation']['weather']
    temp = float(parsed_json['current_observation']['temp_f'])
    full_temp = parsed_json['current_observation']['temperature_string']

    print(f"It is currently {weather} in {citystate}\n\t...{full_temp} ...")

    def custommessage(temp):
        if temp < 50:
            return "\t\t\tIt's cold!"
        else:
            return "\t\t\tIt's nice out... go outside HOMEBOY!"
    print(custommessage(temp))


if __name__ == '__main__':
    Application