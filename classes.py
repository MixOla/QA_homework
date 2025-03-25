class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def run_car(self):
        return "Автомобиль заведен"

    def stop_car(self):
        return "Автомобиль заглушен"

    def get_year(self):
        return self.year

    def get_type(self):
        return self.type

    def get_color(self):
        return self.color