# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

class MyComplexNumber:
    x_class: float
    y_class: float

    def __init__(self, x_class, y_class):
        self.x_class = x_class
        self.y_class = y_class

    def __add__(self, other):
        return MyComplexNumber(self.x_class + other.x_class, self.y_class + other.y_class)

    def __mul__(self, other):
        return MyComplexNumber(self.x_class * other.x_class + self.y_class * other.y_class * -1,
                               self.x_class * other.y_class + self.y_class * other.x_class)

    def __str__(self):
        return f"({self.x_class}{'+' if self.y_class > 0 else ''}{self.y_class}j)"


x_complex = MyComplexNumber(1, 2)
y_complex = MyComplexNumber(3, 4)

print(f"\n\x1b[34m>>>\x1b[0m Метод сложения: {x_complex + y_complex}")
print(f"\x1b[34m>>>\x1b[0m Метод умножения: {x_complex * y_complex}")
