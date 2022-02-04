# Написать декоратор для логирования типов позиционных аргументов функции, например:
# def type_logger...
#     ...
#
#
# @type_logger
# def calc_cube(x):
#    return x ** 3
#
# >>> a = calc_cube(5)
# 5: <class 'int'>
# Примечание: если аргументов несколько - выводить данные о каждом через запятую; можете ли вы вывести тип значения функции?
# Сможете ли решить задачу для именованных аргументов? Сможете ли вы замаскировать работу декоратора? Сможете ли вывести имя функции, например, в виде:
# >>> a = calc_cube(5)
# calc_cube(5: <class 'int'>)

def type_logger(func):
    def wrapper(*args, **kwargs):
        result = f'{func.__name__}('
        for el in args:
            if result[-1] != '(':
                result += ', '
            result += f'{el}: {type(el)}'
        for el in kwargs:
            if result[-1] != '(':
                result += ', '
            result += f'{kwargs[el]}: {type(kwargs[el])}'
        result += ')'
        return result

    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


res = calc_cube(5)
print(res)
