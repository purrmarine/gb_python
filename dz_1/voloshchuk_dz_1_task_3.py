# Реализовать склонение слова «процент» во фразе «N процентов». Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100
for i in range(1, 101):
    if i % 10 in (5, 6, 7, 8, 9, 0) or i in (11, 12, 13, 14):
        print(i, 'процентов')
    elif i % 10 == 1:
        print(i, 'процент')
    else:
        print(i, 'процентa')