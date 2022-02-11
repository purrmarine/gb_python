# 3. Осуществить программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс «Клетка».
# В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число). В классе должны
# быть реализованы методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение
# (__mul__()), деление (__floordiv__, __truediv__()). Эти методы должны применяться только к клеткам и выполнять увеличение,
# уменьшение, умножение и округление до целого числа деления клеток, соответственно.

class Cell:
    def __init__(self, cell_count):
        self.cell_count = cell_count

    def __add__(self, other):
        return Cell(self.cell_count + other.cell_count)

    def __sub__(self, other):
        if (self.cell_count <= other.cell_count):
            raise ValueError(
                "Вычитание невозможно, количество ячеек второй клетки больше либо равно количеству ячеек первой клетки")
        return Cell(self.cell_count - other.cell_count)

    def __mul__(self, other):
        return Cell(self.cell_count * other.cell_count)

    def __floordiv__(self, other):
        return Cell(self.cell_count // other.cell_count)

    def __truediv__(self, other):
        return Cell(self.cell_count // other.cell_count)

    def make_order(self, cnt):
        res = ''
        for i in range(self.cell_count):
            res += '*'
            if (i + 1) % cnt == 0:
                res += '\n'
        return res


cell_1 = Cell(21)
cell_2 = Cell(6)

print(cell_1.make_order(5))

cell_5 = cell_1 + cell_2
cell_6 = cell_1 - cell_2
cell_7 = cell_1 * cell_2
cell_8 = cell_1 / cell_2

print(cell_5.cell_count)
print(cell_6.cell_count)
print(cell_7.cell_count)
print(cell_8.cell_count)
