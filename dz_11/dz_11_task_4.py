# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
# уникальные для каждого типа оргтехники.

class Warehouse:
    '''Склад'''


class OfficeEquipment:
    def __init__(self, name, brand, price, color, height, width, depth, weight, max_paper_size):
        self.name = name
        self.brand = brand
        self.price = price
        self.color = color
        self.height = height
        self.width = width
        self.depth = depth
        self.weight = weight
        self.max_paper_size = max_paper_size


class Printer(OfficeEquipment):
    def __init__(self, name, brand, price, color, height, width, depth, weight, max_paper_size, printer_type,
                 print_speed):
        super().__init__(name, brand, price, color, height, width, depth, weight, max_paper_size)
        self.printer_type = printer_type
        self.print_speed = print_speed


class Scanner(OfficeEquipment):
    def __init__(self, name, brand, price, color, height, width, depth, weight, max_paper_size, scan_type, scan_speed):
        super().__init__(name, brand, price, color, height, width, depth, weight, max_paper_size)
        self.scan_type = scan_type
        self.scan_speed = scan_speed


class Xerox(OfficeEquipment):
    def __init__(self, name, brand, price, color, height, width, depth, weight, max_paper_size, printer_type,
                 print_speed, scan_type, scan_speed):
        super().__init__(name, brand, price, color, height, width, depth, weight, max_paper_size)
        self.printer_type = printer_type
        self.print_speed = print_speed
        self.scan_type = scan_type
        self.scan_speed = scan_speed


printer_1 = Printer('Pantum M6500', 11430, 'black', 417, 224, 305, 7.5, 'A4', 'laser', 20)
printer_2 = Printer('HP Ink Tank 115', 11290, 'black', 523, 284, 138.5, 3.4, 'A4', 'inkjet', 16)
scanner_1 = Scanner('HP Scanjet Enterprise Flow 5000 s5', 57690, 'white', 310, 198, 190, 3.8, 'A4', 'CIS', 25)
xerox_1 = Xerox('Canon imageRUNNER 2206', 55190, 'white', 622, 589, 502, 28.7, 'A3', 'laser', 20, 'flatbed', 23)

warehouse_1 = Warehouse()
