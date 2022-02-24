# 2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...) и возвращающую курс
# этой валюты по отношению к рублю. Использовать библиотеку requests. В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp.
# Рекомендация: выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа.
# Можно ли, используя только методы класса str, решить поставленную задачу? Функция должна возвращать результат числового типа, например float.
# Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal? Сильно ли усложняется код функции при этом?
# Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None. Можно ли сделать работу функции не зависящей от того,
# в каком регистре был передан аргумент? В качестве примера выведите курсы доллара и евро.
from requests import get
from decimal import Decimal


def currency_rates(code):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    s = response.text

    idx_code = s.find('<CharCode>' + code.upper() + '</CharCode>')
    if idx_code == -1:
        return None

    nom_start = s.find('<Nominal>', idx_code) + 9
    nom_end = s.find('</Nominal>', idx_code)

    nominal = s[nom_start:nom_end]

    val_start = s.find('<Value>', idx_code) + 7
    val_end = s.find('</Value>', idx_code)

    value = s[val_start:val_end].replace(',', '.')

    return Decimal(value) / int(nominal)


print("Курс доллара: ", currency_rates("usd"))
print("Курс евро: ", currency_rates("EUR"))
