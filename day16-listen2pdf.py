'''
Function:       Convert PDF to MP3
Date:           02.17.2019
Created By:     Anonymous Systems
Dependencies:   PyPDF2, gtts
'''
import PyPDF2
import re
import os
import sys
from gtts import gTTS


def listen2PDF(filepath):
    f = open(filepath, 'rb')
    filename = os.path.basename('/Users/anonymousone/Documents/MEGA/Books/hack-yourself-first-final.pdf').replace('.pdf', '.mp3')
    pdf = PyPDF2.PdfFileReader(f)
    pdf_num_pages = pdf.getNumPages()
    string_words = ''
    for page_num in range(pdf_num_pages):
        page = pdf.getPage(page_num)
        content = page.extractText()
        textonly = re.findall(r'[a-zA-Z0-9]+', content)
        for word in textonly:
            string_words = string_words + ' ' + word
    print(f'Creating mp3 file {filename}')
    tts = gTTS(text=string_words, lang='en')
    tts.save(filename)
    print(f'Successfully created {filename}, open it to listen to PDF')
    f.close()


if __name__ == '__main__':
    sys.setrecursionlimit(1500)
    filepath = input('Enter PDF filepath: ')
    listen2PDF(filepath)