'''
Function:       Monitor Web Server Access logs for IP address and number of views
Date:           02.05.2019
Created By:     Anonymous Systems
'''


def monitorLog(logfile):
    ip_addresses = {}
    open_file = open(logfile, 'r').readlines()
    for line in open_file:
        ip = line.split(' ')[0]
        if 6 < len(ip) <= 15:
            ip_addresses[ip] = ip_addresses.get(ip, 0) + 1
    print(ip_addresses)


if __name__ == '__main__':
    logfile = '/var/log/nginx/access.log'
    monitorLog(logfile)
