'''
Function:       Perform a Google Search from the command line to receive website links
Date:           02.05.2019
Created By:     Anonymous Systems
'''
from googlesearch import search


def searchGoogle(query):
    for url in search(query, stop=20):
        print(url)


if __name__ == '__main__':
    query = input('What would you like to search for? ')
    searchGoogle(query)
