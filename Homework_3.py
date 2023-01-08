# 1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык.

print('Задача 1')

dictionary_eng_rus = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}
def num_translate(number):
    return dictionary_eng_rus.get(number)

print(num_translate(input('Type number in english to get translation: ')))

# 3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
# в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы

print()
print('Задача 3')

def thesaurus(*args):
    dictionary_alf_names = {}
    for names in args:
        if dictionary_alf_names.get(names[0]):
            dictionary_alf_names[names[0]].append(names)
        else:
            dictionary_alf_names[names[0]] = [names]
    return dictionary_alf_names

print(thesaurus("Иван", "Мария", "Петр", "Илья"))

# 5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
# взятых из трёх списков (по одному из каждого)

print()
print('Задача 5')
"""Вводим набор слов"""
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
"""Начинаем случайный выбор"""
from random import choice

"""Создаём функцию"""
def get_jokes(j, flag=False):
    for i in range(j):
        """Создаём элементы"""
        random_nou = choice(nouns)
        random_adv = choice(adverbs)
        random_adj = choice(adjectives)
        """Задаём очерёдность"""
        jokes = f'{random_nou} {random_adv} {random_adj}'
        """Создаём список, в котором будут отображаться шутки"""
        container = []
        """По заданию, добавляем флаг, который позволит запретить повторы в словах"""
        if flag == True:
            container = jokes.split()
            """Для существительных"""
            for nou in nouns:
                for joke in container:
                    if nou == joke:
                        nouns.remove(nou)
            """Для наречий"""
            for adv in adverbs:
                for joke in container:
                    if adv == joke:
                        adverbs.remove(adv)
            """Для прилагательных"""
            for adj in adjectives:
                for joke in container:
                    if adj == joke:
                        adjectives.remove(adj)
            print(container)
"""Проверяем работу функции. Запрашиваем 2 шутки с запретом повторов слов"""
get_jokes(j = 2, flag=True)