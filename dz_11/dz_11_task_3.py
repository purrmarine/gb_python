# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Запрашивать у пользователя данные и заполнять список необходимо
# только числами. Класс-исключение должен контролировать типы данных элементов списка.

class MyException(Exception):
    pass


my_list = []
print('Enter \'stop\' for exit')
while True:
    num = input('Enter number: ')
    if num == 'stop':
        break
    else:
        try:
            num_1 = num.replace('.', '', 1)
            if not num_1.isdigit() and not (num_1.startswith('-') and num_1.replace('-', '', 1).isdigit()):
                raise MyException('Error, list must contain only numbers')
        except (ValueError, MyException) as err:
            print(err)
        else:
            x = int(num) if num.isdigit() else float(num)
            my_list.append(x)

print(my_list)
