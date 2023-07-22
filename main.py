import telebot
import cfg
import handlers

#123
if __name__ == '__main__':

    # Регистрируем бота
    bot = telebot.TeleBot(cfg.TG_TOKEN)

    # Устанавливаем обработчики
    handlers.set_handlers(bot)

    # Запускаем бота + костыль против ошибок
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as _ex:
            print(_ex)
