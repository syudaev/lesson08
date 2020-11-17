# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
# ситуацию и не завершиться с ошибкой.

class MyDivision:
    divider: float
    divided: float

    def __init__(self, divider, divided):
        self.divider = divider
        self.divided = divided

    def user_division(self):
        if self.divided == 0:
            raise MyZeroDivErr(self.divided)
        else:
            return self.divider / self.divided


class ChekNum:
    def __init__(self, user_string: str):
        self.user_string = user_string

    @staticmethod
    def chek_num(user_string):
        """ ввод строки, проверка и обработка ввода значений численного типа и возврат числа int или float """
        while True:
            user_chek = input(user_string)
            if user_chek.isdigit():
                user_chek = int(user_chek)
                return user_chek
            try:
                user_chek = float(user_chek)
                return user_chek
            except ValueError:
                print(f"\x1b[31m>>>\x1b[0m Ошибка! Вводите только числа!")


class MyZeroDivErr(Exception):
    def __init__(self, user_div: float):
        self.user_div = user_div

    def __str__(self):
        return f"\x1b[31m>>>\x1b[0m Debugging information, cannot be divided by zero >>> {int(self.user_div)}"


string_chek = ChekNum("")

user_class = MyDivision(string_chek.chek_num("Введите число делитель >>> "),
                        string_chek.chek_num("Введите число делимое >>> "))

try:
    print(f"\x1b[34m>>>\x1b[0m Результат деления {user_class.user_division():.2f}")
except MyZeroDivErr as exception:
    print(f"\n\x1b[31m>>>\x1b[0m Внимание! На ноль делить нельзя >>> (делимое = {int(exception.user_div)})")
