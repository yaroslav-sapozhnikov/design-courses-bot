from dal.connection import conn

# метод для получения всех услуг из базы данных
def get_offers():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM offer")
    offers = cursor.fetchall()
    return offers
