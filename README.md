># Домашняя работа _Принципы ООП: Инкапсуляция, наследование, полиморфизм_
>># ФИО: _Столбовой Егор Васильевич_
>># Группа: _Программист | выходные | 19.12.2023_ 
# Описание проекта: "Горячие напитки"

Проект представляет собой простую реализацию классов для работы с продуктами и горячими напитками на языке программирования Python. Программа создает наследника класса `Product` под названием `HotDrink`, добавляя дополнительное поле для температуры напитка.

## Классы

### 1. Класс `Product`

Класс `Product` представляет общие характеристики продукта.

#### Атрибуты:

- `name`: Название продукта.
- `price`: Цена продукта.

#### Методы:

- `__init__(self, name, price)`: Конструктор класса.
- `__str__(self)`: Метод для строкового представления объекта.

### 2. Класс `HotDrink`

Класс `HotDrink` является наследником класса `Product` и добавляет дополнительное поле для температуры напитка.

#### Дополнительные атрибуты:

- `temperature`: Температура горячего напитка.

#### Методы:

- `__init__(self, name, price, temperature)`: Конструктор класса, вызывает конструктор родительского класса.
- `__str__(self)`: Переопределенный метод для строкового представления объекта, включая температуру.

## Пример использования

```python
if __name__ == "__main__":
    # Создаем объекты класса HotDrink
    tea = HotDrink("Чай", 50, 80)
    coffee = HotDrink("Кофе", 100, 90)
    cocoa = HotDrink("Какао", 80, 85)

    # Печатаем информацию о горячих напитках
    print(tea)
    print(coffee)
    print(cocoa)
