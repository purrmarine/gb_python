# Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
list = []
for i in range(1, 1000, 2):
    list.append(i**3)
print(list)

# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
sum_num = 0
for el in list:
    sum_dig = 0
    j = el
    while j % 10 > 0:
        sum_dig += j % 10
        j = j // 10
    if sum_dig % 7 == 0:
        sum_num += el
print(sum_num)

# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
sum_num = 0
for el in list:
    el += 17
    sum_dig = 0
    j = el
    while j % 10 > 0:
        sum_dig += j % 10
        j = j // 10
    if sum_dig % 7 == 0:
        sum_num += el
print(sum_num)
