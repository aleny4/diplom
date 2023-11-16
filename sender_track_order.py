# Алёна Маслова, 10-я когорта - Финальный проект. Инженер по тестированию плюс

# Импорт необходимых пакетов
import sender_stand_request

# Получение заказа по треку
def get_track_number_order():
    track_number = sender_stand_request.create_new_order()
    return track_number.json()["track"]

# Проверяем, что код ответа равен 200
def test_create_and_track_new_order():
    track_number = get_track_number_order()
    get_response = sender_stand_request.info_order(track_number)
    assert get_response.status_code == 200