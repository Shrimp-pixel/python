# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод
# draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из
# классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный
# метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки", end=" ")


class Pen(Stationery):
    def draw(self):
        super().draw()
        print("ручкой")


class Pencil(Stationery):
    def draw(self):
        super().draw()
        print("карандашом")


class Handle(Stationery):
    def draw(self):
        super().draw()
        print("маркером")


pen, pencil, handle = Pen("ручка"), Pencil("карандаш"), Handle("маркер")
pen.draw()
pencil.draw()
handle.draw()
