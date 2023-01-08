# 2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...)
# и возвращающую курс этой валюты по отношению к рублю.

print('Задача 2')
print('')

import requests
def currency_rates(char_code='', URL='http://www.cbr.ru/scripts/XML_daily.asp'):
    respond = requests.get(URL)
# Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None.
    if not (char_code and URL):
        return None
# Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент?
    char_code = char_code.upper()
    if respond.ok:
        currency = respond.text.split(char_code)
        if len(currency) == 1:
            return None
#  Можно ли, используя только методы класса str, решить поставленную задачу?
        value = currency[1].split('</Value>')[0].split('<Value>')[1]
# Функция должна возвращать результат числового типа, например float.
        value = float(value.replace(',', '.'))
# есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal? Сильно ли усложняется код функции при этом?
#        import decimal
#        decimal.getcontext().prec = 4
#        value = decimal.Decimal(value.replace(',', '.'))
        return (value)
    else:
        return None

print(currency_rates(input('Введите буквенный код валюты: ')), '- курс этой валюты по отношению к рублю')

# 4. Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего задания.

print('')
print('Задача 4')
print('')
# Создать скрипт, в котором импортировать этот модуль
import sys
import utils

if __name__ == "__main__":
    char_code = sys.argv[1:]
    for info in char_code:
        currency = utils.currency_rates(info)
        print(currency)