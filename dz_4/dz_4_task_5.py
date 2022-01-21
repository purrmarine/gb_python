import sys
import utils

if len(sys.argv) == 1:
    code = input("Enter country code: ")
    rate, date = utils.currency_rates(code)
    print(rate, date)
else:
    rate, date = utils.currency_rates(sys.argv[1])
    print(rate, date)
