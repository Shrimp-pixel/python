# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число». Реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта. Для этого создаёте экземпляры класса (
# комплексные числа), выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного
# результата.


class Complex:
    def __init__(self, real_part, imaginary_part):
        self.real_part, self.imaginary_part = real_part, imaginary_part

    def __add__(self, other):
        a = self.real_part + other.real_part
        b = self.imaginary_part + other.imaginary_part
        return Complex(a, b)

    def __mul__(self, other):
        a = self.real_part * other.real_part - self.imaginary_part * other.imaginary_part
        b = self.real_part * other.imaginary_part - self.imaginary_part * other.real_part
        return Complex(a, b)

    def __str__(self):
        if self.imaginary_part<0:
            return str(self.real_part) + str(self.imaginary_part) + "i"
        else:
            return str(self.real_part) + "+" + str(self.imaginary_part) + "i"


com1 = Complex(6, -5)
com2 = Complex(2, 4)
print(com1)
print(com2)
print(com1+com2)
print(com1*com2)
