class Rectangle:
    "Класс прямоугольника"
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return f"Площадь прямоугольника - {self.width * self.height}"

    def get_perimetr(self):
        return f"Периметр прямоуголника - {(self.width + self.height)*2}"

rect_1 = Rectangle(2, 4)
print(rect_1.get_square())
print(rect_1.get_perimetr())

rect_2 = Rectangle(7, 10)
print(rect_2.get_square())
print(rect_2.get_perimetr())

rect_3 = Rectangle(1, 14)
print(rect_3.get_square())
print(rect_3.get_perimetr())

class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return f"{self.a} + {self.b} = {self.a + self.b}"

    def multiplication (self):
        return f"{self.a} * {self.b} = {self.a * self.b}"

    def division(self):
        if self.b != 0:
            return f"{self.a} / {self.b} = {self.a / self.b}"
        else:
            return "На ноль делить нельзя"

    def subtraction(self):
        return f"{self.a} - {self.b} = {self.a - self.b}"

num = Math(7, 4)
print(num.division())
print(num.multiplication())
print(num.subtraction())
print(num.addition())

class Button():
    def __init__(self, text):
        self.text = text
        self.type = "Кнопка"
        self.locator = " "


    def get_text(self):
        return self.text
    def click(self):
        return f"Клик по кнопке {self.text}"

button = Button("Радиокнопка")
print(button.get_text())
print(button.click())


