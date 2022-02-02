# Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
# Написать скрипт, который собирает все шаблоны в одну папку templates, например:
# |--my_project
#    ...
#   |--templates
#    |   |--mainapp
#    |   |  |--base.html
#    |   |  |--index.html
#    |   |--authapp
#    |      |--base.html
#    |      |--index.html
# Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках (они играют роль пространств имён);
# предусмотреть возможные исключительные ситуации; это реальная задача, которая решена, например, во фреймворке django.
import os
import shutil

project_name = 'my_project'
prj_dir = os.path.join(os.path.dirname(__file__), project_name)

tpl_dir = os.path.join(prj_dir, 'templates')
if not os.path.exists(tpl_dir):
    os.makedirs(tpl_dir)

for root, dirs, files in os.walk(prj_dir):
    if root.count('templates'):
        for dir in dirs:
            templ = os.path.join(tpl_dir, dir)
            if not os.path.exists(templ):
                os.makedirs(templ)

        for file in files:
            templ_file = os.path.join(tpl_dir, os.path.basename(root), file)
            if not os.path.exists(templ_file):
                shutil.copy(os.path.join(root, file), templ_file)
