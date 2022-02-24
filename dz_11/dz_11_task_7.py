# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число». Реализуйте перегрузку методов
# сложения и умножения комплексных чисел. Проверьте работу проекта. Для этого создаёте экземпляры класса (комплексные числа),
# выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
import re


class ComplexNumber:
    def __init__(self, number):
        self.number = number
        self.a, self.b = self.separate()

    def __add__(self, other):
        a = self.a + other.a
        b = self.b + other.b
        if b < 0:
            res = f'{a}{b}i'
        else:
            res = f'{a}+{b}i'
        return ComplexNumber(res)

    def __mul__(self, other):
        a = (self.a * other.a) + (self.b * other.b) * (-1)
        b = sum([self.a * other.b, self.b * other.a])
        if b < 0:
            res = f'{a}{b}i'
        else:
            res = f'{a}+{b}i'
        return ComplexNumber(res)

    def __str__(self):
        return self.number

    def separate(self):
        m = re.search('[+-]{0,1}[0-9]*i', self.number)
        a = self.number.replace(m.group(0), '')
        b = m.group(0).replace('i', '')
        if a == '':
            a = 0
        if b in ('', '-', '+'):
            b += '1'
        return int(a), int(b)


c_n_1 = ComplexNumber('5-5i')
c_n_2 = ComplexNumber('6-i')
c_n_3 = c_n_1 * c_n_2
c_n_4 = c_n_1 + c_n_2

print(c_n_3)
print(c_n_4)
