# 1. Выяснить тип результата выражений

print('Задача 1')

expr_1 = 15 * 3
expr_2 = 15 / 3
expr_3 = 15 // 2
expr_4 = 15 ** 2

print('Тип результата первого выражения:', type(expr_1))
print('Тип результата второго выражения:', type(expr_2))
print('Тип результата третьего выражения:', type(expr_3))
print('Тип результата четвёртого выражения:', type(expr_4))

# 2. Дан список
# ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(' ')
print('Задача 2')
# 2.1. Необходимо его обработать.
print(' ')
print('Задача 2.1. Обработать список')

got_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

def new_value(v):
    if v[0] in '+-':
        return v[0]

i = 0
while i < len(got_list):
    value = new_value(got_list[i])
    if got_list[i].isdigit() or (value and got_list[i][1:].isdigit()):
        if value:
            got_list[i] = value + got_list[i][1:].zfill(2)
        else:
            got_list[i] = got_list[i].zfill(2)
        got_list.insert(i, '"')
        got_list.insert(i + 2, '"')
        i += 2
    i += 1

print(got_list)
print(' ')
print('Задача 2.2. Сформировать из обработанного списка строку')

for i in range(len(got_list)):
    value = got_list.pop(0)
    if value.isdigit():
        got_list.append(f'"{int(value):02d}"')
    elif value[0] == "+" and value[1].isdigit():
        got_list.append(f'"+{int(value):02d}"')
    else:
        got_list.append(value)

print(" ".join(got_list))

# 4. Дан список, содержащий искажённые данные с должностями и именами сотрудников

print(' ')
print('Задача 4. Сформировать и вывести на экран фразы')

name_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

phrases = 'Привет, {}!'

for new_names in name_list:
    print(phrases.format(new_names.split()[-1].title()))

print(' ')
print('Задача 5.')
print(' ')
print('Задача 5.1. Создать список, содержащий цены на товары (10–20 товаров)')

prices = [57.8, 46.51, 97, 0.99, 55, 5987.5, 654.0, 66, 64, 648.31]

print(prices)
print(' ')
print('Задача 5.2. Вывести на экран эти цены через запятую в одну строку')

ending: str = ", "

for i, number in enumerate(prices):
    determined = str(f"{float(number):.2f}").split(".")
    if i == len(prices) - 1:
        ending = "\n"
    print(f"{determined[0]} руб. {determined[1]} коп.", end=ending)
print(' ')
print('Задача 5.3. Вывести цены, отсортированные по возрастанию')

prices.sort()

print(prices)
print('В коде отсутствует создание нового списка - лишь метод "sort" в отношении ранее созданного списка.')
print(' ')
print('Задача 5.4. Создать новый список, содержащий те же цены, но отсортированные по убыванию.')

prices_desc = prices.copy()

prices_desc.sort(reverse=True)

print(prices_desc)
print(' ')
print('Задача 5.5. Вывести цены пяти самых дорогих товаров.')

print(prices[-5:])