import telebot
from find import bm
import os
import requests
from scripts import download_tiktok
bot = telebot.TeleBot('1035416381:AAHtMVVnm-oxv3MIJyy1SyRRG9cLhtarpSc')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Hi, I'm very glad that you wrote me, please send me an url of your video!")

@bot.message_handler(content_types=['text'])
def send_text(message):
    if bm(message.text.lower(),"tiktok.com")==True:
                bot.send_message(message.chat.id, 'Got a vaild Tiktok link!')

                path = download_tiktok(message.text)
                if path == 0:
                    bot.send_message(message.chat.id, 'Wrong url!')
                else:
                    bot.send_message(message.chat.id, 'Here is your video!')
                    bot.send_video(message.chat.id, open(path, 'rb'), supports_streaming=True)
                    os.remove(path)

    elif bm(message.text.lower(),"instagram.com")==True:
        bot.send_message(message.chat.id, 'Got a vaild instagram link!')
    elif bm(message.text.lower(),"vk.com")==True:
        bot.send_message(message.chat.id, 'Got a vaild Vk link!')
    else:
        bot.send_message(message.chat.id, 'Wrong url!')

@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    bot.send_message(message.chat.id, "Nice stiker!")

bot.polling()




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

    data = {
        'url': link
    }

    response = requests.post(
        'https://tiktokdownloader.net/download_ajax/', data=data)
    soup = BeautifulSoup(response.text, 'html.parser')

    arr = soup.findAll('a')
    print(arr)
    contenturl = arr[0]
    contenturl = str(contenturl)
    contenturl = contenturl.split('href="')
    contenturl = contenturl[1].split('" rel')
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
