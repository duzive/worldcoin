import random
import time

import requests


class WorldCoin(object):
    __slots__ = ('__group_id', '__token', '__base_url')

    def __init__(self, group_id, token):
        """
        :param group_id: ID группы(владельца токена)
        :param token: Токен, полученный в приложении
        """
        self.__group_id = group_id
        self.__token = token
        self.__base_url = 'https://coin.world-coin-game.ru/server/api.php'

    def _send_request(self, params: dict):
        response = requests.get(self.__base_url, json=params).json()
        print(response)
        if not response['status']:
            raise Exception(response['error'])
        return response

    def get_payment_link(self, amount=100, code=random.randint(1, 12345678), lock=0):
        """

        :param amount: сумма
        :param code: код, вернется вам в истории переводов
        :param lock: возможность менять сумму
        :return: Ссылка для получения перевода
        """
        link = f'vk.com/app7614516#pay_{self.__group_id}_{amount}_{code}_{lock}'
        return link

    def get_merchant_balance(self):
        params = {
            "action": "balance",
            "group_id": self.__group_id,
            "token": self.__token
        }
        return self._send_request(params)['coins']

    def get_history_transactions(self, count=10, filter=1):
        """

        :param count: кол-во транзакций
        :param filter: тип транзакций
        :return: массив транзакций
                """
        params = {
            "action": "history",
            "group_id": self.__group_id,
            "token": self.__token,
            "count": count,
            "filter": filter
        }
        return self._send_request(params)['history']

    def send_transfer(self, to_id, amount, code=random.randint(1, 12345678)):
        """

        :param to_id: Получатель
        :param amount: Сумма
        :param code: Код, вернется в транзакии
        :return: Результат выполнения
        """
        params = {
            "action": "transaction",
            "group_id": self.__group_id,
            "token": self.__token,
            "to": to_id,
            "amount": amount,
            "code": code
        }
        return self._send_request(params)

    def get_users_info(self, *args):
        """

        :param args: список игроков через запятую
        :return: Массив словарей
        """
        if len(args) > 100:
            raise ValueError('Массив players не может принимать более 100 игроков за запрос!')
        params = {
            "action": "players",
            "group_id": self.__group_id,
            "token": self.__token,
            "players": args
        }
        return self._send_request(params)['players']

    def custom_request(self, base_params=True, **kwargs):
        """

        :param base_params: Передача стандартных параметров, bool
        :param kwargs: дополнительные параметры
        """
        if base_params:
            base_params_ = {
                "group_id": self.__group_id,
                "token": self.__token
            }
            kwargs.update(base_params_)
        return self._send_request(kwargs)


class LongPolling(object):
    __slots__ = ('__api', '__last_transactions')

    def __init__(self, api_object):
        """

        :param api_object: ваш объект WorldCoin
        """
        self.__api = api_object
        self.__last_transactions = self.__api.get_history_transactions()

    def listen(self, sleep=3):
        """

        :param sleep: Время "засыпания"
        :return: Итератор
        """
        while True:
            history = self.__api.get_history_transactions()
            if history[0] != self.__last_transactions:
                for payment in history:
                    yield payment

                else:
                    self.__last_transactions = history[0]

            time.sleep(sleep)
