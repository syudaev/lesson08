# Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. Проверить
# работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список только числами.
# Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу
# скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный список с числами выводится на
# экран.
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки. При вводе пользователем
# очередного элемента необходимо реализовать проверку типа элемента и вносить его в список, только если введено число.
# Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение. При
# этом работа скрипта не должна завершаться.
class MyNumber:
    user_string: str

    def __init__(self, user_string: str):
        self.user_string = user_string

    @staticmethod
    def my_func(user_string):
        my_bool = True
        my_list = []
        while my_bool:
            str_list = input(user_string).split()
            for i in range(len(str_list)):
                if str_list[i] == 'stop':
                    my_bool = False
                    break
                try:
                    if str_list[i].isdigit():
                        my_list.append(int(str_list[i]))
                    elif str_list[i].replace('.', '', 1).isdigit():
                        my_list.append(float(str_list[i]))
                    elif isinstance(str_list[i], str):
                        raise MyChekStringError(str_list[i])
                except MyChekStringError as exception:
                    print(f"\x1b[31m>>>\x1b[0m Внимание! Введены не числа >>> \x1b[31m{exception.user_str}\x1b[0m")
            print(f"\x1b[34m>>>\x1b[0m Текущий список чисел: {my_list}")
        return my_list


class MyChekStringError(Exception):
    def __init__(self, user_str):
        self.user_str = user_str

    def __str__(self):
        return f"\x1b[31m>>>\x1b[0m >>> !!! Debugging information !!! >>> {self.user_str}"


my_number = MyNumber("")

print(f"\n\x1b[34m>>>\x1b[0m Итоговый список чисел : "
      f"{my_number.my_func('Введите данные через пробел для заполнения списка чисел (завершить: stop) >>> ')}")
