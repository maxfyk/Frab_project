import telebot
import os
from scripts import download_tiktok
bot = telebot.TeleBot('1035416381:AAHtMVVnm-oxv3MIJyy1SyRRG9cLhtarpSc')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Hi, I'm very glad that you wrote me, please send me an url of your video!")

@bot.message_handler(content_types=['text'])
def send_text(message):
    if "tiktok.com" in message.text:
                bot.send_message(message.chat.id, 'Got a vaild Tiktok link! It will take some time to downlaod it ;)')
                path,user,music_info = download_tiktok(message.text)
                if path == False:
                    bot.send_message(message.chat.id, 'Something went wrong')
                else:
                    bot.send_message(message.chat.id, 'Here is your video by '+user+'!')
                    bot.send_video(message.chat.id, open(path, 'rb'), supports_streaming=True)
                    if music_info == False:
                        pass
                    else:
                        bot.send_message(message.chat.id, 'By the way the song is '+music_info[1]+' by '+music_info[0]+'.')

                        bot.send_message(message.chat.id, '<a>You can listen it on </a><a href="'+music_info[2]+'">Apple music</a><a> and </a><a href="'+music_info[3]+'">Spotify</a><a>.</a>',parse_mode="html")

                    os.remove(path)

    elif "instagram.com" in message.text:
        bot.send_message(message.chat.id, 'Got a vaild instagram link!')
    elif "vk.com" in message.text:
        bot.send_message(message.chat.id, 'Got a vaild Vk link!')
    else:
        bot.send_message(message.chat.id, 'Wrong url!')

@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    bot.send_message(message.chat.id, "Nice stiker!")

bot.polling()
