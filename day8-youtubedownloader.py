'''
Function:       Download Song, Video or Playlist from Youtube
Date:           02.09.2019
Created By:     Anonymous Systems
Dependencies:   requests, youtube-dl, ffmpeg
'''
from __future__ import unicode_literals
from requests import get
import youtube_dl
import sys


class Logger(object):
    def debug(self, msg): pass

    def warning(self, msg): pass

    def error(self, msg): print(msg)


def mp4Hook(d):
    # if d['status'] == 'downloading':
    #     print(f"\rDownloading {d['filename']}, ETA {d['_eta_str']}")
    if d['status'] == 'finished':
        print(f"Finsihed downloading {d['filename']}")


mp4_config = {
    'format': 'mp4',
    'logger': Logger(),
    'progress_hooks': [mp4Hook]
}


def mp3Hook(d):
    # if d['status'] == 'downloading':
    #     print(f"\rDownloading {d['filename']}, ETA {d['_eta_str']}")
    if d['status'] == 'finished':
        print(f"Finsihed downloading {d['filename']}, now converting to mp3...")


mp3_config = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'logger': Logger(),
    'progress_hooks': [mp3Hook]
}


def downloadYT(config, url):
    checkurl = 'https://www.youtube.com/oembed?format=json&url=' + url
    r = get(checkurl)
    status_code = r.status_code
    if status_code == 200:
        with youtube_dl.YoutubeDL(config) as ydl:
            ydl.download([url])
    elif status_code == 404:
        print('Invalid Youtube URL')


if __name__ == '__main__':
    choice = input('Enter mp3 for songs OR mp4 for videos: ')
    if choice == 'mp3':
        config = mp3_config
    elif choice == 'mp4':
        config = mp4_config
    else:
        print('INAVLID OPTION')
        sys.exit(1)
    url = input("Paste url here & press enter: ")
    downloadYT(config, url)