# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police(булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.

class Car:
    is_police = False

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self, speed=60):
        self.speed = speed
        print(f'{self.name} - Поехали!')

    def stop(self):
        self.speed = 0
        print(f'{self.name} - Приехали!')

    def turn(self, direction):
        print(f'{self.name} - Повернули {direction}')

    def show_speed(self):
        print(f'Текущая скорость для {self.name}: {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Превышение скорости!')
        print(f'Текущая скорость для {self.name}: {self.speed}')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Превышение скорости!')
        print(f'Текущая скорость для {self.name}: {self.speed}')


class PoliceCar(Car):
    is_police = True


car_1 = PoliceCar(60, 'white', 'Audi')
car_2 = WorkCar(50, 'blue', 'BMW')
car_3 = TownCar(30, 'red', 'Toyota')
car_4 = SportCar(80, 'black', 'Ferrari')

print(car_1.is_police)
print(car_2.is_police)
print(car_2.color)

car_1.turn('налево')

car_3.stop()
car_3.show_speed()
car_3.go()
car_3.show_speed()

car_1.show_speed()
car_2.show_speed()
car_4.show_speed()
