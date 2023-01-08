import sys

DATA_FILE = "./bakery.csv"

revenue_in = list(map(lambda a: f'{float(a):100.2f}', filter(lambda b: b.replace('.', '').isdigit(), sys.argv[1:])))

with open(DATA_FILE, 'w', encoding='utf-8') as sales_book:
    print(*revenue_in, sep='\n', file=sales_book)

place = sys.argv[1]
revenue_new = sys.argv[2]

if not (place.isdigit() and revenue_new.replace('.', '').isdigit()):
    sys.exit(1)

place = int(place)
revenue_new = float(revenue_new)

with open(DATA_FILE, 'r+', encoding='utf-8') as sales_book:
    no_symbols = 0
    for i in range(place-1):
        try:
            no_symbols += len(next(sales_book))
        except StopIteration:
            print('Not in list')
            sys.exit(1)
    sales_book.seek(no_symbols)
    sales_book.writelines(f'{revenue_new:100.2f}')
