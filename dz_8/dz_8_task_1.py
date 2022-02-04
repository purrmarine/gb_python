# 1. Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает имя пользователя и почтовый домен из email адреса и возвращает их в виде словаря. Если адрес не валиден, выбросить исключение ValueError. Пример:
# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   ...
#     raise ValueError(msg)
# ValueError: wrong email: someone@geekbrainsru
# Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении; имеет ли смысл в данном случае использовать функцию re.compile()?
import re


def email_parse(email):
    is_valid = re.match(r'(^[A-z0-9_.+-]+@[A-z0-9-]+\.[A-z0-9.-]{2,}$)', email)
    if is_valid:
        my_dict = {}
        username = re.search(r'^[A-z0-9_.+-]+@', email).group(0)[:-1]
        domain = re.search(r'@[A-z0-9-]+\.[A-z0-9.-]{2,}$', email).group(0)[1:]

        my_dict['username'] = username
        my_dict['domain'] = domain

        return my_dict
    else:
        msg = f'wrong email: {email}'
        raise ValueError(msg)


print(email_parse('someone@geekbrains.ru'))
