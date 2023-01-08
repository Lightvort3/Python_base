# 1. Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt

print('Задача 1')
print('')

def unparsing_file(file_name):
    with open(file_name) as file:
        for line in file:
            remote_adress = line.split(' - - ')[0]
            request_type_and_requested_resource = line.split('"')[1]
            request_type = request_type_and_requested_resource.split()[0]
            requested_resource = request_type_and_requested_resource.split()[1]
            yield(remote_adress, request_type, requested_resource)

if __name__ == '__main__':
    server = unparsing_file('./nginx_logs.txt')
    for logs in server:
        print(logs)

# 3 Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби. ... Написать код, загружающий данные из обоих файлов и формирующий из них словарь

print('')
print('Задача 3')
print('')

def gen_vocabulary(key, value):
    len_value = len(value)
    return ((key_unit, value[i]) if i < len_value else (key_unit, None) for i, key_unit in enumerate(key))

import json
def uniting(
        vocabulary='./vocabulary.txt',
        users='./users.txt',
        hobby='./hobby.txt'):
    with open(users, 'r', encoding='utf-8') as users_txt:
        user_records = users_txt.readlines()
    with open(hobby, 'r', encoding='utf-8') as hobby_txt:
        hobby_records = hobby_txt.readlines()
    if len(user_records) < len(hobby_records):
        return 1
    union = {}
    for name, activity in gen_vocabulary(user_records, hobby_records):
        name = name.replace('\n', '').replace(',', ' ')
        union[name] = activity.replace('\n', '') if activity else None
    with open(vocabulary, 'w', encoding='utf-8') as vocfile:
        vocfile.write(json.dumps(union, indent=4, ensure_ascii=False))
    print(union)

voc = uniting(
    vocabulary='./vocabulary.txt',
    users='./users.txt',
    hobby='./hobby.txt')
print(voc)

# 6 Реализовать простую систему хранения данных о суммах продаж булочной.

print('')
print('Задача 6')
print('')

import add_sale
import show_sales