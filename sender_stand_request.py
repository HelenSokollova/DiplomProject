import configuration
import requests

# функция для создания заказа c заданным телом
def create_order(order_body):
   return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=order_body)

# функция получения информации о заказе по его трек-номеру
def get_order_info_by_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.TAKE_TRACK_PATH + str(track))

