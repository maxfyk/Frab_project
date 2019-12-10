from bs4 import BeautifulSoup
import requests
import os
import wget
from find import bm
import urllib3,requests

def download_tiktok(link):

    http = urllib3.PoolManager()
    print(link)
    r = http.request('GET',link)
    r = r.status
    if 400<=r >= 200:
                pass
    elif r == 404:
                return 0
    if bm(link,"vm.tiktok.com") == True:
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        r = requests.get(link, headers=headers)

        for resp in r.history:
            link =   r.url
    print(link)
    link = "https://www.tiktok.com/@sannioksanen/video/6761026382500842758"
    response = requests.get(link)
    print(response.text)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup)
    contenturl =  soup.find_all("video").get("src")
    print(contenturl)

    name = str(link).split("/")[-1]

    return save_video(contenturl[0], name + ".mp4")

def save_video(link, name):
    cwd = str(os.getcwd())

    try:
        os.mkdir(cwd + "\\Videos")
    except:
        pass

    cwd += "\\Videos\\"

    path = cwd + name
    wget.download(link, path)

    return path
