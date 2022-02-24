# 3. Доработать функцию currency_rates(): теперь она должна возвращать кроме курса дату, которая передаётся в ответе сервера.
# Дата должна быть в виде объекта date. Подумайте, как извлечь дату из ответа, какой тип данных лучше использовать в ответе функции?
from requests import get
from decimal import Decimal
from datetime import datetime


def currency_rates(code):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    s = response.text

    date_start = s.find("Date=") + 6
    date_end = s.find("\"", date_start)
    date_str = s[date_start:date_end]
    rate_date = datetime.date(datetime.strptime(date_str, '%d.%m.%Y'))

    idx_code = s.find('<CharCode>' + code.upper() + '</CharCode>')
    if idx_code == -1:
        return None, rate_date

    nom_start = s.find('<Nominal>', idx_code) + 9
    nom_end = s.find('</Nominal>', idx_code)

    nominal = s[nom_start:nom_end]

    val_start = s.find('<Value>', idx_code) + 7
    val_end = s.find('</Value>', idx_code)

    value = s[val_start:val_end].replace(',', '.')

    return Decimal(value) / int(nominal), rate_date


rate, date = currency_rates("usd")
print(f"Курс доллара на {date}: {rate}")

rate, date = currency_rates("EUR")
print(f"Курс евро на {date}: {rate}")
