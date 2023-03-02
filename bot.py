from telebot import *
from buttons import *
import os
#import youtube_dl
import yt_dlp


TOKEN = 'add ur token'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])

def start_message(message):
  bot.send_message(message.chat.id,"Выберите от куда вы хотите скачать видео.", reply_markup = social_network)



@bot.callback_query_handler(func=lambda call: True)

def choose_social_network(call):
  if call.data == 'INS':
        bot.send_message(call.message.chat.id, 'Пока не Работает:(')

  elif call.data == 'YT':
      bot.send_message(call.message.chat.id, '👋 Пришлите ссылку на YouTube видео и я его скачаю для вас ❤️‍🔥')


      @bot.message_handler()

      def YOUTUBE_DOWNLOADER(message):

        link = message.text
        ydlopts = {
            'outtmpl': '%(id)s.%(ext)s',
        }
        with yt_dlp.YoutubeDL(ydlopts) as ydl:
            video = ydl.extract_info(
                link,
                download=False
            )
        videoname = video['title']
        ydl.download([link])
        filename = ydl.preparefilename(video)

        bot.senddocument(message.chat.id, open(filename, 'rb'),
            caption='Here is your video: {}'.format(videoname))

        os.remove(filename)

bot.infinity_polling()
