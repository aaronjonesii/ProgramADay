'''
Function:       Check to see if websites return status code 200 for up and running
Date:           02.05.2019
Created By:     Anonymous Systems
'''
from requests import get


def checkWebsites(websites):
    for website in websites:
        if 'http' not in website:
            website = 'http://' + website
        try:
            r = get(website)
            if r.status_code == 200:
                print(f'[ {website} ]\t - \t√ UP & RUNNING({r.status_code})')
                # print(r.content)
            else:
                print(f'[ {website} ]\t - \tRETURNED STATUS CODE: {r.status_code}')
        except Exception as e:
            print(f'[ {website} ]\t > \t{e}')


if __name__ == '__main__':
    websites = [
        'anonsys.tech',
        'api.anonsys.tech',
    ]
    checkWebsites(websites)
