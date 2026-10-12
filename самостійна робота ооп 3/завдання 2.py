n = int(input("Введіть кількість вершин ділянки узбережжя: "))

if n < 3:
    print("Помилка: многокутник повинен мати щонайменше 3 вершини.")
else:
    points = []

    for i in range(n):
        print(f"\nВершина {i + 1}:")
        x = float(input("x = "))
        y = float(input("y = "))
        points.append((x, y))

    area = 0

    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]

        area += x1 * y2 - y1 * x2

    area = abs(area) / 2

    print("\nПлоща ділянки узбережжя:", area)

    if area < 50:
        print("Ділянка невелика.")
    elif area < 200:
        print("Ділянка середнього розміру.")
    else:
        print("Ділянка велика.")