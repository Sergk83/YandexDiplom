#Сергей Комаров, 10-ая когорта Финальный проект, инженер по тестированию плюс
import sender_stand_request

# Запрос на создание нового заказа
def test_order_creation():
    creation_response = sender_stand_request.post_new_order()
    track_id = creation_response.json()['track'] # Извлекаем 'track' из JSON jndtnf
    response = sender_stand_request.get_orders_track(track_id) # получение информации о заказе по 'track'
    assert response.status_code == 200  # Проверка, что статус код ответа равен 200