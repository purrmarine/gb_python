# Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield

def gen_num(n):
    for i in range(1, n + 1, 2):
        yield i


num = gen_num(9)
for el in num:
    print(el)
