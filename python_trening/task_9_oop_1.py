from python_trening.task_9_checks import Checks


class Class1(Checks):
    def __init__(self, loc, param1):
        super().__init__(loc) # Инициализируем родительский класс
        self.param1 = param1

class Class2(Checks):
    def __init__(self, loc, param2):
        super().__init__(loc) # Инициализируем родительский класс
        self.param2 = param2

class Class3(Checks):
    def __init__(self, loc, param3):
        super().__init__(loc) # Инициализируем родительский класс
        self.param3 = param3


class Class4(Checks):
    def __init__(self, loc, param4):
        super().__init__(loc) # Инициализируем родительский класс
        self.param4 = param4



# Создаем объекты и вызываем метод check_text()
obj1 = Class1("loc1", "value1")
obj2 = Class2("loc2", "value2")
obj3 = Class3("loc3", "value3")
obj4 = Class4("loc4", "value4")

print(obj1.check_text()) # Вывод: loc1
print(obj2.check_text()) # Вывод: loc2
print(obj3.check_text()) # Вывод: loc3
print(obj4.check_text()) # Вывод: loc4