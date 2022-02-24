# 1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
# >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"
# Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить информацию, необходимую для перевода: какой тип данных выбрать, в теле функции или снаружи.

def num_translate(eng_num):
    numerals = {"zero": "ноль",
                "one": "один",
                "two": "два",
                "three": "три",
                "four": "четыре",
                "five": "пять",
                "six": "шесть",
                "seven": "семь",
                "eight": "восемь",
                "nine": "девять",
                "ten": "десять"}
    if eng_num in numerals:
        rus_num = numerals[eng_num]
    else:
        rus_num = None
    return rus_num


num = input("please write a number from zero to ten: ")
print(num_translate(num))
