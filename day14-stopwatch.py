'''
Function:       CLI Stopwatch
Date:           02.17.2019
Created By:     Anonymous Systems
Dependencies:
'''
from sys import stdout as s
import time
import datetime


def wrapper():
    s.write(f'StopWatch by AnonymousOne | {datetime.datetime.now()} \n')


def stopwatch():
    s.write("Clock started: \n\n")
    n = 1
    s.flush()
    while True:
        try:
            # s.write('')
            s.write(f'{n} secs \r')
            n += 1
            s.flush()
            time.sleep(1)
        except KeyboardInterrupt:
            s.write("\n\nExiting program now... \n")
            s.write("Total time: %d secs \n" % (n))
            s.write('\n')
            break


if __name__ == '__main__':
    wrapper()
    stopwatch()
