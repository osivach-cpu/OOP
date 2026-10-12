print("SHORELINE TOTTORI")
print("Таблиця оцінок персонажів та кількість оцінок 3")
print()

n = int(input("Введіть кількість персонажів: "))

characters = []

for i in range(n):
    print()
    print("Персонаж №", i + 1)

    name = input("Введіть ім'я персонажа: ")

    grades = list(map(int, input("Введіть 4 оцінки через пробіл: ").split()))

    characters.append([name, grades])

print()
print("ТАБЛИЦЯ ПЕРСОНАЖІВ")
print("-" * 60)
print(f"{'№':<5}{'Імя':<20}{'Оцінки':<20}{'Кількість 3':<15}")
print("-" * 60)

for i in range(n):
    name = characters[i][0]
    grades = characters[i][1]

    count_three = grades.count(3)

    print(f"{i + 1:<5}{name:<20}{str(grades):<20}{count_three:<15}")

print("-" * 60)