import math

print("Shoreline Tottori")
print("Розрахунок параметра ігрової події")
print()

x = float(input("Введіть значення x: "))

if 4.0 <= x < 2:
    y = x * math.sqrt(x - 5)
    print(f"Значення функції y = {y:.4f}")

elif 2 <= x < 8:
    y = math.atan(x ** 2)
    print(f"Значення функції y = {y:.4f}")

elif x >= 8:
    y = math.log10(abs(x)) - 7.8
    print(f"Значення функції y = {y:.4f}")

else:
    print("Для введеного значення x функція не визначена.")