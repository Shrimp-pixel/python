# 5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и
# передачу в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру (например, словарь).


class Office_Equipment:
    def __init__(self, model, param1, param2, param3):
        self.model = model
        self.parm1 = param1
        self.parm2 = param2
        self.parm3 = param3


class Printer(Office_Equipment):
    def __init__(self, model, param1, param2, param3, paramprint):
        super().__init__(model, param1, param2, param3)
        self.paramprint = paramprint


class Scanner(Office_Equipment):
    def __init__(self, model, param1, param2, param3, paramscan):
        super().__init__(model, param1, param2, param3)
        self.paramscan = paramscan


class Xerox(Office_Equipment):
    def __init__(self, model, param1, param2, param3, paramxerox):
        super().__init__(model, param1, param2, param3)
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
