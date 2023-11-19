# Сергей Комаров, 10-ая когорта Финальный проект, инженер по тестированию плюс
import configuration
import requests
import data


def post_new_order():  # Создание нового заказа
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_NEW_ORDER,  # url
                         json=data.order_body)  # тело


def get_orders_track(track_id):  # Получение заказа по его трек номеру
    return requests.get(configuration.URL_SERVICE + configuration.RECEIVING_ORDER_BY_ID + "?t=" + str(track_id))
