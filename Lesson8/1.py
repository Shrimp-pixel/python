# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать
# число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить
# валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных
# данных.


class Data:
    def __init__(self, date):
        self.date = date

    @classmethod
    def transmutation(cls, date):
        a = date.split("-")
        day, month, year = a
        day = int(day)
        month = int(month)
        year = int(year)
        print(type(day), type(month), type(year))

    @staticmethod
    def valid(day, month):
        day, month = int(day), int(month)
        if month > 12 or month < 1:
            print("inval")
            return False
        if day < 1 or (
                month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12) and day > 31 \
                or (month == 4 or month == 6 or month == 9 or month == 8 or month == 9 or month == 11) and day > 30 \
                or month == 2 and day > 28:
            print("inval")
            return False
        print("Val")
        return True


myd1 = Data("12-12-1999")
myd2 = Data("12-31-1999")
myd3 = Data("32-01-1999")
Data.transmutation(myd1.date)
print(myd1.valid(myd1.date.split("-")[0], myd1.date.split("-")[1]))
print(myd2.valid(myd2.date.split("-")[0], myd2.date.split("-")[1]))
print(myd3.valid(myd3.date.split("-")[0], myd3.date.split("-")[1]))
