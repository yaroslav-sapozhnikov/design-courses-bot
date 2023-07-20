import telebot
from time import sleep

if __name__ == '__main__':

    bot = telebot.TeleBot("6319313381:AAHkSPxDujZfFGqZJ7U7SnL3MjoFXVVL7fs")

    @bot.message_handler(content_types=['text'])
    def msg_handling(event):

        print("Получено сообщение: " + event.text)

        if event.text == '/start':
            bot.send_message(event.chat.id, 'Привет, иди нахуй')

        elif event.text.lower() == 'диск':
            bot.send_message(event.chat.id, 'https://docs.google.com/document/d/1mqWcUILB1WOEsodbewQKx_sDXy1diWNCbojuVZ148oE/edit')

        else:
            bot.send_message(event.chat.id, f'Я не знаю, что значит "{event.text}", поэтому иди нахуй')


    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as _ex:
            print(_ex)
