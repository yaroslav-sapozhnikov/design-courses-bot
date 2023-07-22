import dal.offer_repository as offer_repo


# сервис, в котором содержится бизнес-логика обработки сообщения от пользователя
def get_offers(bot, event):
    # вызываем метод репозитория, который лезет в БД
    offers = offer_repo.get_offers()

    # формируем сообщение, куда запихиваем данные, полученные из БД
    msg = f"Привет, у нас есть следующие услуги:"
    for i in range(len(offers)):
        msg += f"""

{offers[i][1]}
Цена: {offers[i][2]} руб.
    """

    # отправляем сообщение
    bot.send_message(event.chat.id, msg)
