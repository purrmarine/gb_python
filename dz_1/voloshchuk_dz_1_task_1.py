# 1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration
# в секундах: до минуты: <s> сек; до часа: <m> мин <s> сек; до суток: <h> час <m> мин <s> сек;
# * в остальных случаях: <d> дн <h> час <m> мин <s> сек.

duration = int(input('Enter duration: '))
result = ''

d = duration // 86400
if d > 0:
    duration = duration % 86400
    result += str(d) + ' дн '

h = duration // 3600
if h > 0 or result != '':
    duration = duration % 3600
    result += str(h) + ' час '

m = duration // 60
if m > 0 or result != '':
    duration = duration % 60
    result += str(m) + ' мин '

result += str(duration) + ' сек'

print(result)

