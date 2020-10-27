WorldCoin 1.0.0
=================================================================================================================================================================================
**worldcoin** - это модуль для упрощенной работы с api WorldCoin

#### Установка модуля
```bash
python -m pip install worldcoin_wrapper
```

Работа с модулем
---
#### Быстрый старт
```python /* или python3 */
from worldcoin import WorldCoin

Seccion = WorldCoin(group_id=12345678, token="token")
```
* `group_id` - ID владельца токена
* `token` - Токен, выданный вам в приложении

### Методы 

#### get_payment_link
***Получение ссылки для принятия переводов***
```python /* или python3 */
Seccion.get_payment_link(amount=100, code=1234, lock=0)
```
* `amount` - сумма перевода(По умолчанию: 100)
* `code` - вернется вам в истории(Если не указан: от 1 до 12345678)
* `lock` - Возможность редактирования суммы(По умолчанию: 0) 

#### get_merchant_balance
***Получение баланса мерчанта***
```python /* или python3 */
Seccion.get_merchant_balance()
```


#### get_history_transactions
***Получение истории переводов***
```python /* или python3 */
Seccion.get_history_transactions(count=15, filter=1)
```
* `count` - количество переводов(По умолчанию: 10)
* `filter` - фильтр операций(По умолчанию: 1)


#### send_transfer
***Перевод коинов пользователю***
```python /* или python3 */
Seccion.send_transfer(to_id=12345678, amount=100, code=1234)
```
* `to_id` - получатель перевода
* `point` - сумма перевода
* `code` - вернется в списке платежей(Если не указан: от 1 до 12345678)

#### get_users_info
***Получение данных игроков***
```python /* или python3 */
Seccion.get_user_info(282952551, 12345678)
```
* ID указываются через запятую

#### Кастомный запрос - custom_request
***Если вы не обнаружили необходимого вам метода в стандартных, 
стоит использовать кастомный метод***
##### Для примера, получим баланс мерчанта, используя кастомный метод
```python /* или python3 */
Seccion.custom_request(base_params=True, action="balance")
```
* `base_params` - передача базовых параметров, таких как group_id и token(По умолчанию: True)
* Все параметры передаются подобно action


### LongPolling
***Модуль нативно поддерживает LongPolling, 
для его использования требуется реализовать новый дочерний класс: LongPolling***
```python /* или python3 */
from worldcoin import LongPolling

LongPoll = LongPolling(Seccion)
```

##### Следующие действия просты, необходимо использовать метод listen в цикле, для активации LongPoll
```python /* или python3 */
for payment in VKPointPool(VKPointSession).listen(sleep = 5):

    user_id = payment['from']
    amount = payment['amount']

    print(f'Получен платёж на сумму {amount} от {user_id}')
```
* Вот так просто ;)
### Дополнительно

* [Разработчик](http://vk.com/duzive)
* [Исходный код](worldcoin_wrapper/worldcoin.py)
* [Официальная документация](https://worldcoin.docs.apiary.io/#/reference/история-переводов)