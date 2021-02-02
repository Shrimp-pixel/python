# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных,
# вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не
# завершиться с ошибкой.


class Error(Exception):
    def __init__(self, txt):
        self.txt = txt



while True:
    try:
        a = int(input("Делимое: "))
        b = int(input("Делитель: "))
        if b == 0:
            raise Error("Деление на ноль запрещено")
        print(a/b)
        break
    except Error as err:
        print(err)