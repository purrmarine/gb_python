# Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp
# Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?); как лучше хранить конфигурацию
# этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект; можно ли будет при этом расширять
# конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?

import os

ROOT = os.path.dirname(__file__)
dir_names = ['my_project',
             'my_project/settings',
             'my_project/mainapp',
             'my_project/adminapp',
             'my_project/authapp']
for dir_name in dir_names:
    dir_path = os.path.join(ROOT, dir_name)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
