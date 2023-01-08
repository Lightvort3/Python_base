DATA_FILE = "./bakery.csv"

def data_read(begin=-1, finish=-1):
    with open(DATA_FILE, 'r', encoding='utf-8') as sales_book:
        if begin > 0:
            for i in range(begin - 1):
                sales_book.readline()
        if finish > 0:
            for i in range(abs(finish - begin) + 1):
                yield sales_book.readline().replace('\n', '')
        else:
            for row in sales_book:
                yield row.replace('\n', '')

if __name__ == '__main__':
    import sys
    begin_place = -1
    finish_place = -1
    if len(sys.argv) >= 2 and sys.argv[1].isdigit():
        begin_place = int(sys.argv[1])
    if len(sys.argv) == 3 and sys.argv[2].isdigit():
        finish_place = int(sys.argv[1])
    for c in data_read(begin_place, finish_place):
        print(f'{float(1):.2f}')