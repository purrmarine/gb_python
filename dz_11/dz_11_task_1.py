# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и
# года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Date:
    def __init__(self, str_date):
        self.str_date = str_date
        self.day, self.month, self.year = self.date_to_number(self.str_date)

    @classmethod
    def date_to_number(cls, str_date):
        day = int(str_date[:str_date.find('-')])
        month = int(str_date[str_date.find('-') + 1:str_date.rfind('-')])
        year = int(str_date[str_date.rfind('-') + 1:])
        cls.validate(day, month, year)
        return day, month, year

    @staticmethod
    def validate(d, m, y):
        month_dict = {1: 31,
                      2: 29,
                      3: 31,
                      4: 30,
                      5: 31,
                      6: 30,
                      7: 31,
                      8: 31,
                      9: 30,
                      10: 31,
                      11: 30,
                      12: 31}
        if y < 1000 or y > 3000:
            raise ValueError('year error')
        if m not in month_dict:
            raise ValueError('month error')
        elif d not in range(1, month_dict[m] + 1) or (m == 2 and y % 4 != 0 and d not in range(1, month_dict[m])):
            raise ValueError('day error')


d_1 = Date('12-06-2021')
print(d_1.day, d_1.month)

d_2 = Date('31-06-2021')
print(d_2.day)
