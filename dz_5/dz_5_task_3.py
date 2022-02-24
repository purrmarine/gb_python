# Есть два списка:
# tutors = [
#     'Иван', 'Анастасия', 'Петр', 'Сергей',
#     'Дмитрий', 'Борис', 'Елена'
# ]
# klasses = [
#     '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
# ]
# Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>)

def my_gen(tutor, klass):
    for t, k in zip(tutor, klass):
        yield (t, k)
    k = len(tutor) - len(klass)
    if k > 0:
        for t in tutor[-k:]:
            yield t, None


tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Мария', 'Анна', 'Максим']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

result = my_gen(tutors, klasses)
for el in result:
    print(el)
