# Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби. Известно, что при хранении
# данных используется принцип: одна строка — один пользователь, разделитель между значениями — запятая. Написать код,
# загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби. Сохранить
# словарь в файл. Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО,
# задаём в словаре значение None. Если наоборот — выходим из скрипта с кодом «1». При решении задачи считать, что объём
# данных в файлах во много раз меньше объема ОЗУ.
import sys
import json

res_dict = {}
with open('users.csv', encoding='utf-8') as user_file, open('hobby.csv', encoding='utf-8') as hobby_file:
    for user in user_file:
        hobby = hobby_file.readline().strip()
        if hobby == '':
            hobby = None
        res_dict[user.strip()] = hobby
    if hobby_file.readline():
        sys.exit(1)

with open('result.json', 'w', encoding='utf-8') as res_file:
    json.dump(res_dict, res_file, ensure_ascii=False)

with open('result.json', encoding='utf-8') as res_file:
    open_json = json.load(res_file)
print(open_json)
