import pytest
import requests
import URL
import data


# создание заказа
def post_new_order():
    return requests.post(URL.CURRENT_URL + URL.CREATE_NEW_ORDER,
                         json=data.new_order,
                         headers=data.headers)

# токен заказа
def track_number():
    track = post_new_order().json()['track']
    return track


# получение заказа
def test_get_order_number():
    updated_api = URL.GET_ORDER + f"?t={track_number()}"
    get_order = requests.get(URL.CURRENT_URL + updated_api)
    assert get_order.status_code == 200


# Василий Бахметов, 9-ая когорта - Финальный проект. ИНженер по тестированию плюс