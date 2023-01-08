import requests
def currency_rates(char_code='', URL='http://www.cbr.ru/scripts/XML_daily.asp'):
    respond = requests.get(URL)
    if not (char_code and URL):
        return None
    char_code = char_code.upper()
    if respond.ok:
        currency = respond.text.split(char_code)
        if len(currency) == 1:
            return None
        value = currency[1].split('</Value>')[0].split('<Value>')[1]
        value = float(value.replace(',', '.'))
        return (value)
    else:
        return None

print(currency_rates(input('Введите буквенный код валюты: ')), '- курс этой валюты по отношению к рублю')