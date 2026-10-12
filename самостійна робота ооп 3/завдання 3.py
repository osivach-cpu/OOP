n = int(input("Введіть кількість об'єктів на узбережжі: "))

if n <= 0:
    print("Помилка: кількість об'єктів повинна бути додатною.")
else:
    total_mass = 0
    moment_x = 0
    moment_y = 0

    for i in range(n):
        print(f"\nОб'єкт {i + 1}")

        x = float(input("Координата x: "))
        y = float(input("Координата y: "))
        mass = float(input("Маса об'єкта: "))

        if mass <= 0:
            print("Маса повинна бути додатною.")
            break

        total_mass += mass
        moment_x += mass * x
        moment_y += mass * y

    else:
        center_x = moment_x / total_mass
        center_y = moment_y / total_mass

        print("\nЗагальна маса:", total_mass)
        print("Центр мас системи:")
        print("x =", center_x)
        print("y =", center_y)
