# 4. Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения функции и
# выбрасывать исключение ValueError, если что-то не так

def val_checker(callback):
    def _val_checker(func):
        def wrapper(*args):
            for el in args:
                if not callback(el):
                    msg = f'wrong val {el}'
                    raise ValueError(msg)
                return func(*args)

        return wrapper

    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


print(calc_cube(4))
print(calc_cube(0))
