# 1. Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield

print('Задача 1')
print('')

def odd_nums_generator(n):
    n = n - 1
    current = -1
    while current < n:
        current += 2
        yield current

odd_to_15 = odd_nums_generator(15)

print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
#print(next(odd_to_15)) #- на этом наступает Stop iteration

# 3. Есть два списка

print('')
print('Задача 3')
print('')

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
#klasses = [
#    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
#] - такой список в задаче
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А',
] # - сделаем список короче, для выполнения ситуации с 'None"

def tuple_gen():
    return ((tutor, klasses[t])
            if t < len(klasses)
            else (tutor, None)
            for t, tutor in enumerate(tutors))

if __name__ == '__main__':
    print(tuple_gen()) # - проверка, что генератор - это генератор
    res = tuple_gen()
    print(next(res))
    print(next(res))
    print(next(res))
    print(next(res))
    print(next(res))
    print(next(res))
    print(next(res))
#    print(next(gen)) #- на этом наступает Stop iteration

# 4. Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего

print('')
print('Задача 4')
print('')

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = []

for i in range(len(src)-1):
    if src[i] < src[i+1]:
        result.append(src[i+1])

print(result)

# 5. Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.

print('')
print('Задача 5')


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

# напишите сначала решение «в лоб».
print('Решение в лоб')

set_lst = set(src)
print(set_lst)

# Потом подумайте об оптимизации
print('Оптимизация')

got_lst = set()
set_lst_2 = [n for n in src if n not in got_lst and (got_lst.add(n) or True)]
print(set_lst_2)

from collections import Counter
alone = Counter(src)
set_lst_2 = list(alone)
set_lst_3 = [n for n,i in alone.items() if i==1]
print(set_lst_3)