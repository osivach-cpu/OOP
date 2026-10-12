print("Shoreline Tottori")
print("Таблиця розташування об'єктів узбережжя")
print()

m = int(input("Введіть кількість зон узбережжя: "))
n = int(input("Введіть кількість типів об'єктів: "))

matrix = []

print()
print("Введіть значення матриці:")

for i in range(m):
    row = []

    for j in range(n):
        value = float(input(
            f"Зона {i + 1}, об'єкт {j + 1}: "
        ))
        row.append(value)

    matrix.append(row)

print()
print("Початкова матриця:")

for row in matrix:
    print(row)

transposed = []

for j in range(n):
    row = []

    for i in range(m):
        row.append(matrix[i][j])

    transposed.append(row)

print()
print("Транспонована матриця:")

for row in transposed:
    print(row)