import math
print("Shoreline Tottori")
print("Розрахунок параметра узбережжя")
print()

x_start = float(input("Введіть початкове значення x: "))
x_end = float(input("Введіть кінцеве значення x: "))
dx = float(input("Введіть крок dx: "))
if x_start <= 0 or x_end <= 0:
    print("Помилка: для lg(x) значення x повинно бути більше 0.")

elif x_start <= 1 <= x_end:
    print("Помилка: значення x = 1 не можна використовувати,")
    print("оскільки знаменник x^2 - 1 дорівнює нулю.")

elif dx <= 0:
    print("Помилка: крок dx повинен бути більшим за 0.")

elif x_start > x_end:
    print("Помилка: початкове значення x не може бути більшим за кінцеве.")

else:
    x = x_start
    number = 1

    print()
    print(f"{'№':<5}{'x':<12}{'y':<15}")
    print("-" * 32)

    while x <= x_end + 0.000001:

        if x > 0 and x != 1:
            y = 5 * math.log10(x) / (x ** 2 - 1)

            print(f"{number:<5}{x:<12.2f}{y:<15.4f}")

        else:
            print(f"{number:<5}{x:<12.2f}{'не визначено':<15}")

        x += dx
        number += 1