'''
Function:       Loading Bar for CLI
Date:           02.17.2019
Created By:     Anonymous Systems
Dependencies:   tqdm
'''
# from __future__ import print_function
import time
from tqdm import tqdm


def startLoadingBar():
    for i in tqdm(range(10000)):
        time.sleep(0.002)
        pass

if __name__ == '__main__':
    startLoadingBar()