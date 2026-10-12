print("Shoreline Tottori")
print("Аналіз стану об'єктів узбережжя")
print()

n = int(input("Введіть кількість об'єктів: "))

objects = []

for i in range(n):
    value = float(input(f"Введіть значення стану об'єкта №{i + 1}: "))
    objects.append(value)

print()
print("Стан об'єктів:")

positive_objects = []

for i in range(n):
    if objects[i] > 0:
        positive_objects.append(i + 1)

if len(positive_objects) > 0:
    print("Номери динамічних об'єктів:", positive_objects)
else:
    print("Динамічних об'єктів немає.")