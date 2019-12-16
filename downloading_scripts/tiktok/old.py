import time
import os
import wget
from pyvirtualdisplay import Display
from bs4 import BeautifulSoup
import requests
import os
import wget
from find import bm
import urllib3,requests
from lxml import html, etree
import requests

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
        headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36'}
        r = requests.get(link, headers=headers)

        for resp in r.history:
            link =   r.url

        print(link)


    page = requests.get(link)
    extractedHtml = page.content
    print(extractedHtml)
    imageSrc = extractedHtml.xpath("//video/@src")
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(extractedHtml)
    #contenturl =  soup.find_all("video").get("src")
    print(imageSrc)

    name = str(link).split("/")[-1]

    return save_video(imageSrc, name + ".mp4")

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
download_tiktok('https://www.tiktok.com/@sannioksanen/video/6761026382500842758/')

def get_html(video_url):
            chromeProfile = webdriver.ChromeOptions()
            chromeProfile.add_argument("--disable-automation")
            chromeProfile.add_experimental_option(
            "excludeSwitches", ["enable-automation"])
            chromeProfile.add_experimental_option("mobileEmulation", {"deviceName": "Galaxy S5"})
            driver = webdriver.Chrome('b.exe',chrome_options=chromeProfile)
            driver.get(video_url)
            driver.implicitly_wait(5)
            driver.get_screenshot_as_file('evan-profile.png')

            link = driver.find_element_by_xpath("//video").get_attribute("src")

            return save_video(link, 'video' + ".mp4")

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
print(get_html('https://www.tiktok.com/@lucyrobsongolf/video/6726531918118145286'))
import time
import os
import wget
from pyvirtualdisplay import Display
from bs4 import BeautifulSoup
import requests
import os
import wget
from find import bm
import urllib3,requests
from lxml import html, etree
import requests

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
        headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36'}
        r = requests.get(link, headers=headers)

        for resp in r.history:
            link =   r.url

        print(link)


    page = requests.get(link)
    extractedHtml = page.content
    print(extractedHtml)
    imageSrc = extractedHtml.xpath("//video/@src")
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(extractedHtml)
    #contenturl =  soup.find_all("video").get("src")
    print(imageSrc)

    name = str(link).split("/")[-1]

    return save_video(imageSrc, name + ".mp4")

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
download_tiktok('https://www.tiktok.com/@sannioksanen/video/6761026382500842758/')

def get_html(video_url):
            chromeProfile = webdriver.ChromeOptions()
            chromeProfile.add_argument("--disable-automation")
            chromeProfile.add_experimental_option(
            "excludeSwitches", ["enable-automation"])
            chromeProfile.add_experimental_option("mobileEmulation", {"deviceName": "Galaxy S5"})
            driver = webdriver.Chrome('b.exe',chrome_options=chromeProfile)
            driver.get(video_url)
            driver.implicitly_wait(5)
            driver.get_screenshot_as_file('evan-profile.png')

            link = driver.find_element_by_xpath("//video").get_attribute("src")

            return save_video(link, 'video' + ".mp4")

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
print(get_html('https://www.tiktok.com/@lucyrobsongolf/video/6726531918118145286'))
