import requests
import os
import wget
from find import bm
from selenium import webdriver

data = {
'url': 'https://mphw-suse1.muscdn.com/reg02/original_track/2018/02/03/20/81ca8ea5-6a6c-4cb6-97dd-993c7966663e_iYehXJLNkK.m4a',
'return': 'timecode,apple_music,spotify',
'api_token': '3d38517124f625f0b1aed001f45fe58d'
}

result = requests.post('https://api.audd.io/', data=data)
data = result.json()
data = data["result"]
artist = data["artist"]
title = data["title"]
apple_music = data["apple_music"]["url"]
spotify = data["spotify"]["external_urls"]["spotify"]
music_info = [artist,title,apple_music,spotify]
print(music_info[3])
