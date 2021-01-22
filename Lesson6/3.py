# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии
# (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return int(self._income["wage"]) + int(self._income["bonus"])


fistPosition = Position("Name1", "Surname1", "Position1", 1000, 100)
secondPosition = Position("Name2", "Surname2", "Position2", 2000, 200)
thirdPosition = Position("Name3", "Surname3", "Position3", 3000, 300)
fourthPosition = Position("Name3", "Surname4", "Position4", 4000, 400)

print(fistPosition.get_full_name())
print(secondPosition.get_full_name())
print(thirdPosition.get_full_name())
print(fourthPosition.get_full_name())
print(fistPosition.get_total_income())
print(secondPosition.get_total_income())
print(thirdPosition.get_total_income())
print(fourthPosition.get_total_income())

