x = float(input("Введіть координату x хвилі ( від -1 до 1): "))
n = int(input("Введіть ступінь полінома n: "))

if x < -1 or x > 1:
    print("Помилка: x повинен бути в межах від -1 до 1.")
elif n < 0:
    print("Помилка: n не може бути від'ємним.")
else:
    if n == 0:
        result = 1
    elif n == 1:
        result = x
    else:
        t0 = 1
        t1 = x

        for i in range(2, n + 1):
            t2 = 2 * x * t1 - t0
            t0 = t1
            t1 = t2

        result = t1

    wave_height = abs(result) * 3

    print("Значення полінома Чебишева:", result)
    print("Розрахована висота хвилі:", wave_height)

    