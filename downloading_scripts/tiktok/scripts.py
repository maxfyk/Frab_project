import requests
import os
import wget
from selenium import webdriver
cwd = str(os.getcwd())
def download_tiktok(link):

    if "vm.tiktok.com" in link:
        headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36'}
        r = requests.get(link, headers=headers)

        for resp in r.history:
            link =   r.url

    chromeProfile = webdriver.ChromeOptions()
    chromeProfile.add_argument("--disable-automation")

    chromeProfile.add_experimental_option(
    "excludeSwitches", ["enable-automation"])
    chromeProfile.add_argument("headless")

    try:
        driver = webdriver.Chrome('b.exe',chrome_options=chromeProfile)
        driver.get(link)
        driver.implicitly_wait(3)
        user = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/main/div/div[2]/a/div[2]/h2").text
        video_link = driver.find_element_by_xpath("//video").get_attribute("src")
        name = str(video_link).split(".com/")
        name = str(name[1]).split("/")
        name = name[0]
        try:
            driver.find_element_by_xpath("//*[@id='main']/div[2]/div/div/main/div/div[2]/div[1]/p[1]/a").click()
            driver.implicitly_wait(3)
            audio_link = driver.find_element_by_xpath("//*[@id='mse']/video").get_attribute("src")
            artist,title,apple_music,spotify =find_song(audio_link, name)
            music_info = [artist,title,apple_music,spotify]
        except:
            music_info = False
            pass

        driver.close()
        print (video_link)

        print(user)

        path = save_video(video_link, name)

        return path,user,music_info
    except:
        return False,False,False


def save_video(link, name):

    try:

        cwd1 = cwd+"\\Videos\\"

        path = cwd1 + name+ ".mp4"
        wget.download(link, path)
        return path
    except:
         return False


def find_song(path,name):

    data = {
    'url': path,
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
    return artist,title,apple_music,spotify
#download_tiktok('https://www.tiktok.com/@sannioksanen/video/6761026382500842758/')
