# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
# для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных. Подсказка:
# постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.


class Office_Equipment:
    def __init__(self, model, quantity, param2, param3):
        try:
            self.quantity = int(quantity)
        except ValueError:
            print("Неверное значение")
            return
        self.model = model
        self.parm2 = param2
        self.parm3 = param3


class Printer(Office_Equipment):
    def __init__(self, model, quantity, param2, param3, paramprint):
        super().__init__(model, quantity, param2, param3)
        self.paramprint = paramprint


class Scanner(Office_Equipment):
    def __init__(self, model, quantity, param2, param3, paramscan):
        super().__init__(model, quantity, param2, param3)
        self.paramscan = paramscan


class Xerox(Office_Equipment):
    def __init__(self, model, quantity, param2, param3, paramxerox):
        super().__init__(model, quantity, param2, param3)
        self.paramxerox = paramxerox


class Warehouse:
    def __init__(self, storage=None):
        if storage is None:
            storage = []
        self.storage = list(storage)

    def add(self, obj: Office_Equipment):
        self.storage.append(obj)

    def transfer(self, other, obj):
        try:
            self.storage.remove(obj)
            other.storage.append(obj)
        except Exception:
            print("Ошибка")


xer = Xerox("model1", 5, "param2", "param3", "paramxer")
sca = Scanner("model2", "5", "param2", "param3", "paramscan")
try:
    pri = Printer("model3", "пять", "param2", "param3", "paramprint")
except ValueError:
    pass
warehouse1 = Warehouse()
warehouse1.add(xer)
