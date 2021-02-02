# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер,
# ксерокс). В базовом классе определите параметры, общие для приведённых типов. В классах-наследниках реализуйте
# параметры, уникальные для каждого типа оргтехники.


class Warehouse:
    pass


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
