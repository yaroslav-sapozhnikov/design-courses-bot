import service.offer_service as offer_srv


def set_handlers(bot):
    # обработчик текстовых сообщений
    @bot.message_handler(content_types=['text'])
    def msg_handling(event):

        print("Получено сообщение: " + event.text)

        if event.text == '/start':
            bot.send_message(event.chat.id, 'Привет, иди нахуй')

        # получаем список услуг из БД
        elif event.text.lower() == 'услуги':
            offer_srv.get_offers(bot, event)

        elif event.text.lower() == 'диск':
            bot.send_message(event.chat.id, 'https://docs.google.com/document/d/1mqWcUILB1WOEsodbewQKx_sDXy1diWNCbojuVZ148oE/edit')

        else:
            bot.send_message(event.chat.id, f'Я не знаю, что значит "{event.text}", поэтому иди нахуй')