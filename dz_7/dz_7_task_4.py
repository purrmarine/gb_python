# Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи — верхняя граница размера
# файла (пусть будет кратна 10), а значения — общее количество файлов (в том числе и в подпапках), размер которых не превышает
# этой границы, но больше предыдущей (начинаем с 0), например:
# {
#       100: 15,
#       1000: 3,
#       10000: 7,
#       100000: 2
#}
# Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
# Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.
import os

dir_name = './'

size_dict = {}
for root, dirs, files in os.walk(dir_name):
    for file in files:
        f_path = os.path.join(root, file)
        file_size = os.stat(f_path).st_size

        i = 1
        while file_size > 10:
            file_size /= 10
            i += 1

        if 10 ** i not in size_dict:
            size_dict[10 ** i] = 1
        else:
            size_dict[10 ** i] += 1

size_dict = dict(sorted(size_dict.items()))

print(size_dict)
