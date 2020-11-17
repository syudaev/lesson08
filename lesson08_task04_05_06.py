# -------------------------------- 4 ------------------------
# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# уникальные для каждого типа оргтехники.
# -------------------------------- 5 ------------------------
# Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
# определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других
# данных, можно использовать любую подходящую структуру, например словарь.
# -------------------------------- 6 ------------------------
# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для
# указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: по возможности реализовать в проекте «Склад оргтехники» max возможностей, изученных на уроках по ООП.

class WarehouseOfficeEquipment:
    max_count: int
    equip_list: list
    acc_dep_list: list

    def __init__(self, max_count, equip_list):
        self.max_count = max_count
        self.equip_list = equip_list
        self.acc_dep_list = []


class AccDepartment:
    need_printer: int
    need_scanner: int
    need_copier: int

    def __init__(self, need_printer, need_scanner, need_copier):
        self.need_printer = need_printer
        self.need_scanner = need_scanner
        self.need_copier = need_copier

    @staticmethod
    def print_parameter():
        print(f"\n\x1b[34m>>>\x1b[0m Функция вывода параметров разных устройств оргтехники:")

    @staticmethod
    def moving_equipment():
        print(f"\n\x1b[34m>>>\x1b[0m Потребность отдела бухгалтерии в оргтехнике: ")
        for x in range(len(stock.equip_list)):
            if stock.equip_list[x].setdefault('Модель устройства') == 'Printer':
                print(f" на складе {stock.equip_list[x].get('Модель устройства')} - "
                      f"{stock.equip_list[x].get('Количество')}   потребность - {need_acc.need_printer} "
                      f">>> {'нет' if need_acc.need_printer - stock.equip_list[x].get('Количество') > 0 else 'да'}")
                stock.acc_dep_list.append(stock.equip_list[x])
            elif stock.equip_list[x].setdefault('Модель устройства') == 'Scanner':
                print(f" на складе {stock.equip_list[x].get('Модель устройства')} - "
                      f"{stock.equip_list[x].get('Количество')}   потребность - {need_acc.need_scanner} "
                      f">>> {'нет' if need_acc.need_scanner - stock.equip_list[x].get('Количество') > 0 else 'да'}")
                stock.acc_dep_list.append(stock.equip_list[x])
            elif stock.equip_list[x].setdefault('Модель устройства') == 'Copier':
                print(f" на складе  {stock.equip_list[x].get('Модель устройства')} - "
                      f"{stock.equip_list[x].get('Количество')}   потребность - {need_acc.need_copier} "
                      f">>> {'нет' if need_acc.need_copier - stock.equip_list[x].get('Количество') > 0 else 'да'}")
                stock.acc_dep_list.append(stock.equip_list[x])

        print(f"\n\x1b[34m>>>\x1b[0m Перемещено со склада в отдел бухгалтерии: ")
        for x in range(len(stock.acc_dep_list)):
            y = stock.equip_list[x].setdefault('Количество')
            if stock.acc_dep_list[x].setdefault('Модель устройства') == 'Printer':
                print(
                    f" {stock.acc_dep_list[x].setdefault('Модель устройства')} - "
                    f"{need_acc.need_printer if need_acc.need_printer <= y else y}")
            elif stock.acc_dep_list[x].setdefault('Модель устройства') == 'Scanner':
                print(f" {stock.acc_dep_list[x].setdefault('Модель устройства')} - "
                      f"{need_acc.need_printer if need_acc.need_scanner <= y else y}")
            elif stock.acc_dep_list[x].setdefault('Модель устройства') == 'Copier':
                print(f"  {stock.acc_dep_list[x].setdefault('Модель устройства')} - "
                      f"{need_acc.need_printer if need_acc.need_copier <= y else y}")


class OfficeEquipment:
    model: str
    price: int
    quantity: int
    equipment: dict
    my_store: list

    def __init__(self, model: str, price: int, quantity: int):
        self.model = model
        self.price = price
        self.quantity = quantity
        self.warehouse = []
        self.equipment = {}

    def in_equipment(self):
        current_count = 0
        while True:
            self.model = input('Введите наименование (завершить - stop): ')
            if self.model == 'stop' or self.model == 'q' or self.model == 'й':
                break
            self.price = MyFunctions.chek_num('Введите цену за ед: ')
            self.quantity = MyFunctions.chek_num(f"Введите количество (свободных мест на складе - "
                                                 f"{stock.max_count - current_count}): ")
            try:
                if self.quantity + current_count > stock.max_count:
                    raise CapacityException(self.quantity, stock.max_count)
            except CapacityException:  # as exception:
                print(f"Stock \x1b[31m>>>\x1b[0m Need more {stock.max_count - current_count - self.quantity}")
                continue
            current_count = current_count + self.quantity
            self.equipment = {'Модель устройства': self.model, 'Цена за ед': self.price,
                              'Количество': self.quantity}
            self.equipment.update(self.equipment)
            self.warehouse.append(self.equipment)
        print(f"\n\x1b[34m>>>\x1b[0m Поступившая техника на склад (список из словарей):")
        for x in self.warehouse:
            print(f" {x}")


class Printer(OfficeEquipment):
    resolution: str
    type_printer: str

    def __init__(self, model, price, quantity, resolution, type_printer):
        super().__init__(model, price, quantity)
        self.resolution = resolution
        self.type_printer = type_printer

    @staticmethod
    def print_parameter(attr1: str, attr2: str, attr3: str):
        print(f"\x1b[34m\x1b[0m Model: {attr1}   Разрешение: {attr2}      Технология: {attr3}")


class Scanner(OfficeEquipment):
    color_depth: str
    type_scanner: str

    def __init__(self, model, price, quantity, color_depth, type_scanner):
        super().__init__(model, price, quantity)
        self.color_depth = color_depth
        self.type_scanner = type_scanner

    @staticmethod
    def print_parameter(attr1: str, attr2: str, attr3: str):
        print(f"\x1b[34m\x1b[0m Model: {attr1}   Глубина цвета: {attr2}        Тип: {attr3}")


class Copier(OfficeEquipment):
    copy_volume: str
    cost_sheet: str

    def __init__(self, model, price, quantity, copy_volume, cost_sheet):
        super().__init__(model, price, quantity)
        self.copy_volume = copy_volume
        self.cost_sheet = cost_sheet

    @staticmethod
    def print_parameter(attr1: str, attr2: str, attr3: str):
        print(f"\x1b[34m\x1b[0m Model: {attr1}    Объем копий/мес: {attr2}   "
              f"Себестоимость экземпляра: {attr3}")


class MyFunctions:
    @staticmethod
    def chek_num(user_string):
        """ ввод строки, проверка и обработка ввода значений численного типа и возврат числа int или float """
        while True:
            try:
                user_chek = input(user_string)
                if user_chek.isdigit():
                    user_chek = int(user_chek)
                    return user_chek
                elif user_chek.replace('.', '', 1).isdigit():
                    user_chek = float(user_chek)
                    return user_chek
                elif isinstance(user_chek, str):
                    raise MyChekStringError(user_chek)
            except MyChekStringError:  # as exception:
                print(f"\x1b[31m>>>\x1b[0m Ошибка! Вводите только числа!")


class MyChekStringError(Exception):
    def __init__(self, user_str):
        self.user_str = user_str

    def __str__(self):
        return f"\x1b[31m>>>\x1b[0m >>> !!! Debugging information !!! >>> {self.user_str}"


class CapacityException(Exception):
    def __init__(self, current, needle):
        self.current = current
        self.needle = needle

    def __str__(self):
        return f"Not enough space, current = {self.current}, needle = {self.needle} "


equipment_list = [{'Модель устройства': 'Printer', 'Цена за ед': 15000, 'Количество': 4},
                  {'Модель устройства': 'Scanner', 'Цена за ед': 8000, 'Количество': 4},
                  {'Модель устройства': 'Copier', 'Цена за ед': 9000, 'Количество': 2}]

stock = WarehouseOfficeEquipment(10, equipment_list)
input_equipment = OfficeEquipment("", 0, 0)
need_acc = AccDepartment(3, 5, 8)
parameter_printer = Printer("Pinter", 15000, 0, "", "")
parameter_scanner = Scanner("Scanner", 8000, 0, "", "")
parameter_copier = Copier("Copier", 9000, 0, "", "")

# поступление оргтехники на склад с проверкой достпных мест хранения, ввода числовых значений стоимости и количества
input_equipment.in_equipment()

# передача оргтехники в подразделение с проверкой достпных мест хранения, ввода числовых значений стоимости и количества
need_acc.moving_equipment()

# разные характеристики для каждого типа оргтехники(принтер, сканер, ксерокс).
need_acc.print_parameter()
parameter_printer.print_parameter("Printer", "1200dpi", "laser")
parameter_scanner.print_parameter("Scanner", "24", "tablet")
parameter_copier.print_parameter("Copier", "10000", "90 коп")
