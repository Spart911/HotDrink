class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.price} руб."


class HotDrink(Product):
    def __init__(self, name, price, temperature):
        super().__init__(name, price)
        self.temperature = temperature

    def __str__(self):
        return f"{super().__str__()} ({self.temperature} градусов)"


if __name__ == "__main__":
    # Создаем объекты класса HotDrink
    tea = HotDrink("Чай", 50, 80)
    coffee = HotDrink("Кофе", 100, 90)
    cocoa = HotDrink("Какао", 80, 85)

    # Печатаем информацию о горячих напитках
    print(tea)
    print(coffee)
    print(cocoa)
