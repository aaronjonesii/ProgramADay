'''
Function:       Crawl website for emails
Date:           02.09.2019
Created By:     Anonymous Systems
Dependencies:   requests, bs4
'''
from requests import get
from bs4 import BeautifulSoup
import re


def getEmails(file, url):
    email_pattern = r'[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*'
    page = get(url)
    if page.status_code == 200:
        soup = BeautifulSoup(page.content, 'html.parser')
        emails = soup(text=re.compile(email_pattern))
        if len(emails):
            file.write(f'[ √ ] Found {len(emails)} on {url} => {emails} \n')
        else: file.write(f'Found 0 emails for {url} => {emails} \n')
    else: print(f'Something went wrong => {page.url}/{page.status_code} - {page.content}')


def getLinks(url):
    page = get(url)
    if page.status_code == 200:
        soup = BeautifulSoup(page.content, 'html.parser')
        links = soup.find_all('a', href=True)
        urls = set()
        for a in links:
            if a['href'].startswith('http'):
                urls.add(a['href'])
            elif a['href'].startswith('/'):
                urls.add(url + a['href'])
        return urls


if __name__ == '__main__':
    domain = input('Enter the domain you would like to scrape for emails: ')
    filename = domain
    if 'http' not in domain:
        domain = 'http://' + domain
    urls = getLinks(domain)
    print(f'[!] Found {len(urls)} urls from {domain}')
    file = open(filename + '.txt', 'w')
    for url in urls:
        getEmails(file, url)
    #     print(link)

    print(f'Finished writing emails to {file.name}')