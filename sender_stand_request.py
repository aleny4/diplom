# Алёна Маслова, 10-я когорта - Финальный проект. Инженер по тестированию плюс

# Импорт необходимых пакетов
import requests
import configuration
import data

# POST-запрос на создание нового заказа
def create_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_NEW_ORDER,
           json=data.body_order)

# GET-запрос на получение информации о заказе по его номеру
def info_order(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_INFO,
           params={"t": track_number})