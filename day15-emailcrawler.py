'''
Function:       Crawl website for emails
Date:           02.18.2019
Created By:     Anonymous Systems
Dependencies:   requests, bs4
'''
from requests import get
from bs4 import BeautifulSoup
import re


def getEmails(file, url):
    # email_pattern = r'[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*'
    email_pattern = r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,10}$"
    try:
        page = get(url)
        if page.status_code == 200:
            soup = BeautifulSoup(page.content, 'html.parser')
            emails = soup(text=re.compile(email_pattern))
            if len(emails):
                file.write(f'[ ! ] Found {len(emails)} email(s) on {url} => {emails} \n')
                return emails
            else:
                file.write(f'\tFound 0 emails for {url} => {emails} \n')
                return None
        else: print(f'Something went wrong => {page.url}/{page.status_code} - {page.content}')
    except: print(f'Something went wrong => {url}')


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
    all_emails_found = set()

    for url in urls:
        urlemails = getEmails(file, url)

        if urlemails == None: pass
        elif len(urlemails):
            for email in urlemails:
                all_emails_found.add(email)
    if len(all_emails_found):
        output = f'[ * ] Found a total of {len(all_emails_found)} email(s) => {all_emails_found}'
        print(output)
        file.write(output)
        print(f'Finished writing emails to {file.name}')
    else: print('No emails were found!')

