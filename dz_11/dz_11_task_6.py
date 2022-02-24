# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

class Warehouse:
    '''Склад'''
    product_dict = {}
    department_dict = {}

    def add_product(self, product, cnt):
        self.count_validate(cnt)
        self.product_validate(product)
        if product.name not in self.product_dict:
            self.product_dict[product.name] = 0
        self.product_dict[product.name] += cnt

    def send_to_department(self, department, product, cnt):
        self.count_validate(cnt)
        self.product_validate(product)
        if product.name not in self.product_dict or self.product_dict[product.name] == 0:
            print(f'На складе отсутствует товар "{product.name}"!')
        elif self.product_dict[product.name] < cnt:
            print(f'Товара "{product.name}" на складе недостаточно!')
        else:
            if department not in self.department_dict:
                self.department_dict[department] = {}
            if product.name not in self.department_dict[department]:
                self.department_dict[department][product.name] = 0
            self.department_dict[department][product.name] += cnt  # передаём в подразделение
            self.product_dict[product.name] -= cnt  # убавляем товар на складе

    def count_validate(self, val):
        if type(val) is not int:
            raise ValueError('Error. Incorrect data type for count')

    def product_validate(self, val):
        if type(val) not in (Printer, Scanner, Xerox):
            raise ValueError('Error. Incorrect data type for product')


class OfficeEquipment:
    '''Оргтехника'''

    def __init__(self, name, price, color, height, width, depth, weight, max_paper_size):
        self.name = name
        self.price = price
        self.color = color
        self.height = height
        self.width = width
        self.depth = depth
        self.weight = weight
        self.max_paper_size = max_paper_size


class Printer(OfficeEquipment):
    '''Принтеры'''

    def __init__(self, name, price, color, height, width, depth, weight, max_paper_size, printer_type,
                 print_speed):
        super().__init__(name, price, color, height, width, depth, weight, max_paper_size)
        self.printer_type = printer_type
        self.print_speed = print_speed


class Scanner(OfficeEquipment):
    '''Сканеры'''

    def __init__(self, name, price, color, height, width, depth, weight, max_paper_size, scan_type, scan_speed):
        super().__init__(name, price, color, height, width, depth, weight, max_paper_size)
        self.scan_type = scan_type
        self.scan_speed = scan_speed


class Xerox(OfficeEquipment):
    '''Ксероксы'''

    def __init__(self, name, price, color, height, width, depth, weight, max_paper_size, printer_type,
                 print_speed, scan_type, scan_speed):
        super().__init__(name, price, color, height, width, depth, weight, max_paper_size)
        self.printer_type = printer_type
        self.print_speed = print_speed
        self.scan_type = scan_type
        self.scan_speed = scan_speed


printer_1 = Printer('Pantum M6500', 11430, 'black', 417, 224, 305, 7.5, 'A4', 'laser', 20)
printer_2 = Printer('HP Ink Tank 115', 11290, 'black', 523, 284, 138.5, 3.4, 'A4', 'inkjet', 16)
scanner_1 = Scanner('HP Scanjet Enterprise Flow 5000 s5', 57690, 'white', 310, 198, 190, 3.8, 'A4', 'CIS', 25)
xerox_1 = Xerox('Canon imageRUNNER 2206', 55190, 'white', 622, 589, 502, 28.7, 'A3', 'laser', 20, 'flatbed', 23)

warehouse_1 = Warehouse()
warehouse_1.add_product(printer_1, 5)
warehouse_1.add_product(printer_2, 3)
warehouse_1.add_product(printer_1, 2)
warehouse_1.add_product(scanner_1, 6)

print(warehouse_1.product_dict)

warehouse_1.send_to_department('dep_1', printer_2, 4)
warehouse_1.send_to_department('dep_1', printer_1, 4)
warehouse_1.send_to_department('dep_2', xerox_1, 4)
warehouse_1.send_to_department('dep_2', scanner_1, 4)
warehouse_1.send_to_department('dep_1', scanner_1, 2)

print(warehouse_1.product_dict)
print(warehouse_1.department_dict)
