import sys

# sale_list = []
with open('bakery.csv', 'r', encoding='utf-8') as sale_file:
    #sale_list = sale_file.read().splitlines()

    if len(sys.argv) == 1:
        for sale in sale_file.readlines():
            print(sale, end='')
    elif len(sys.argv) == 2:
        for sale in sale_file.readlines()[int(sys.argv[1])-1:]:
        #for el in sale_list[]:
            print(sale, end='')
    elif len(sys.argv) == 3:
        for sale in sale_file.readlines()[int(sys.argv[1])-1:int(sys.argv[2])]:
            print(sale, end='')


