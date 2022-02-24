# 5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
# (когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?
import random


def get_jokes(n=1, repeat=True):
    """
    Возвращает n шуток, сформированных из трех случайных слов
    """
    result = []
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    for i in range(n):
        noun = random.choice(nouns)
        adverb = random.choice(adverbs)
        adjective = random.choice(adjectives)

        result.append(f'{noun} {adverb} {adjective}')

        if repeat == False and len(nouns) > 0 and len(adverbs) > 0 and len(adjectives) > 0:
            nouns.remove(noun)
            adverbs.remove(adverb)
            adjectives.remove(adjective)
            if len(nouns) == 0 or len(adverbs) == 0 or len(adjectives) == 0:
                print("Закончились слова для шуток")
                break

    return result


print(get_jokes(9))
