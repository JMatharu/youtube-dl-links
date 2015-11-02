__author__ = 'jmatharu'

import requests
import re
from bs4 import BeautifulSoup

def youtube_link_extractor():
    url = input("Paste Playlist URL : ")
    url_filter = url.replace('https://www.youtube.com/playlist?','')
    url_index = '&&index='
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for link in soup.findAll('a', {'class': 'pl-video-title-link'}):
        href = link.get('href')
        filtered_video_front = href.replace('/watch?v=', '')
        filtered_video_link = filtered_video_front.replace(url_filter,'')
        final_link_string = filtered_video_link.replace('&&index=', ' (Video Number) ----> ')
        final_link_string2 = final_link_string.replace('&index=', ' (Video Number) ----> ')
        title = link.string
        print(title +" "+final_link_string2)

youtube_link_extractor()
# &index=4&