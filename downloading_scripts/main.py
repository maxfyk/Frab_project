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
