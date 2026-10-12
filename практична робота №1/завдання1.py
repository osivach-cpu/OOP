import math

class ShorelineTottori:
    def __init__(self, x):
        self.x = x

    def check_x(self):
        if self.x + 2 * math.pi <= 0:
            return False

        if self.x + 2 * math.pi == 1:
            return False

        if math.sin(self.x + 1) + math.atan(math.pi * self.x) < 0:
            return False

        return True

    def calculate(self):
        if not self.check_x():
            print("Для такого x функцію обчислити неможливо.")
            return

        numerator = math.sqrt(
            math.sin(self.x + 1) +
            math.atan(math.pi * self.x)
        )

        denominator = math.log10(self.x + 2 * math.pi)

        y = numerator / denominator - 1

        print("Координата x:", self.x)
        print("Значення функції y:", y)

print("Shoreline TOTTORI")
print("Обчислення координати берегової лінії")

x = float(input("Введіть значення x: "))

shoreline = ShorelineTottori(x)
shoreline.calculate()


