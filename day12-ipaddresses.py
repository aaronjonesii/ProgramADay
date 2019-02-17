'''
Function:       Show External & Internal IP Addresses
Date:           02.17.2019
Created By:     Anonymous Systems
Dependencies:   requests
'''
from requests import get
import socket


def getExternalIP():
    url = 'http://api.anonsys.tech/ip/'
    try:
        request = get(url)
        external_ip = request.json()['content']['ip']
        print(f'WAN IP Address => {external_ip}')
    except Exception as e:
        print(f'Unknown Error => {e}')


def getInternalIP():
    try:
        internal_ip = (socket.gethostbyname(socket.gethostname()))
        print(f'LAN IP Address => {internal_ip}')
    except Exception as e:
        print(f'Unknown Error => {e}')

if __name__ == '__main__':
    getExternalIP()
    getInternalIP()