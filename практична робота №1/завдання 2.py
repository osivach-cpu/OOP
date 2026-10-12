import math

class ShorelineCalculator:
    def __init__(self, x):
        self.x = x
        self.y = 23.41

    def calculate(self):
        value = math.sin(self.x - 1) ** 3 + math.cos(self.y)

        if value < 0:
            print("Помилка: підкореневий вираз менше нуля.")
            print("Для цього значення x розрахунок d неможливий.")
            return None

        d = math.sqrt(value)
        return d

x = float(input("Введіть значення x: "))

shoreline = ShorelineCalculator(x)

d = shoreline.calculate()

if d is not None:
    print("Результат:")
    print("d =", d)