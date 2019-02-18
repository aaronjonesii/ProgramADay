'''
Function:       IP Geolocation
Date:           02.17.2019
Created By:     Anonymous Systems
Dependencies:   requests
'''
from requests import get
import sys


def getIP(ip):
    url = 'http://api.anonsys.tech/ip/' + ip
    try:
        json_ipinfo = get(url).json()['content']
        ip = json_ipinfo['ip']
    except Exception as e:
        print(f'Something went wrong => MAKE SURE YOU ARE PROVIDING AN IP ADDRESS')
        sys.exit(1)
    return (ip, json_ipinfo)


if __name__ == '__main__':
    ip = input('Enter ip address or leave blank: ')
    ip, ip_info = getIP(ip)
    print(f'Displaying information for {ip}')
    # print(ip_info)
    for key, value in ip_info.items():
        print(f'{key.capitalize()} => {value}')