# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (
# булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый
# класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
# переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return "car go"

    def stop(self):
        return "car stop"

    def turn(self, direction):
        return f"car turn {direction}"

    def show_speed(self):
        return self.speed


class TownCar(Car):
    def show_speed(self):
        if int(self.speed) > 60:
            print("Превышении скорости")
        return self.speed


class WorkCar(Car):
    def show_speed(self):
        if int(self.speed) > 40:
            print("Превышении скорости")
        return self.speed


class SportCar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


townCar, sportCar, workCar, policeCar = TownCar(80, "Red", "towncar", False), \
                                        SportCar(110, "Blue", "sportcar", False), WorkCar(50, "Green", "workcar",
                                                                                          False), \
                                        PoliceCar(60, "White", "policecar")
print(townCar.show_speed())
print(sportCar.show_speed())
print(workCar.show_speed())
print(policeCar.show_speed())
print(townCar.name)
print(policeCar.is_police)
