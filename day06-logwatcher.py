'''
Function:       Watch log file to see when a new line have been added
Date:           02.06.2019
Created By:     Anonymous Systems
'''
import sys
import os
import time
from datetime import datetime


def watchFile(filename):
    openfile = open(filename, 'r')
    openfile.seek(0, os.SEEK_END)
    while True:
        logtime = datetime.now().strftime('%c')
        line = openfile.readline()
        if not line:
            time.sleep(0.1)
            continue
        print(f'New Entry on {logtime}: {line}')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python3 logwatcher.py <LOG FILENAME PATH HERE>')
        sys.exit(1)
    filename = sys.argv[1]
    # filename = os.path.join('/Users/anonymousone/Documents/MEGA/Development/Python/New/LogWatcher', 'test.log')
    print(f'Currently watching [ {filename} ]\n')
    watchFile(filename)
