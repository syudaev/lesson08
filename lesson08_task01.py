# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год» В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число,
# месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию
# числа, месяца и года (например, Месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class DateClass:
    date_attr: str

    def __init__(self, date_attr: str = "01-01-2020"):
        self.date_attr = date_attr

    @classmethod
    def date_attr_extract(cls, date_attr: str):
        return [int(n) for n in date_attr.split('-')]

    @staticmethod
    def date_attr_span(date_attr: list):
        d_sm, m_sm, y_sm = date_attr
        if 1 <= d_sm <= 31 and 1 <= m_sm <= 12 and 1900 <= y_sm <= 2020:
            return f"Дата {date_string} введена верно"
        else:
            return f"\x1b[31mВнимание! Дата {date_string} введена не верно\x1b[0m!"

    def __str__(self):
        return f"{self.date_attr}"


date_cm = "29-06-2018"
date_string = DateClass(date_cm)

print(f"\n"
      f"\x1b[34m>>>\x1b[0m Дата {date_string} передается как атрибут в DateClass")
print(
    f"\x1b[34m>>>\x1b[0m Число, месяц, год извлечены из {date_cm} и преобразованы к типу «Число» в списке >>> "
    f"{date_string.date_attr_extract(date_cm)}")
print(f"\x1b[34m>>>\x1b[0m\x1b[0m {date_string.date_attr_span(date_string.date_attr_extract(date_cm))}")

date_cm = input("\n\x1b[34mВведите дату в формате дд-мм-гггг: \x1b[0m")
date_string = DateClass(date_cm)

try:
    print(f"\x1b[34m>>>\x1b[0m {date_string.date_attr_span(date_string.date_attr_extract(date_cm))}")
except ValueError:
    print(f"\x1b[31mВнимание! Дата введена не в формате дд-мм-гггг!\x1b[0m")
