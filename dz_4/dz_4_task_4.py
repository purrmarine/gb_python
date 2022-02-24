import utils

rate, date = utils.currency_rates("AMD")
print(f'Курс армянского драма на {date}: {rate}')

rate, date = utils.currency_rates("BYN")
print(f'Курс белорусского рубля на {date}: {rate}')

rate, date = utils.currency_rates("KZT")
print(f'Курс казахстанского тенге на {date}: {rate}')
