class GameObject:
    def __init__(self, name, source, location, year):
        self.name = name
        self.source = source
        self.location = location
        self.year = year


def save_to_file(objects, filename):
    with open(filename, "w", encoding="utf-8") as file:
        for obj in objects:
            file.write(
                f"{obj.name}|{obj.source}|{obj.location}|{obj.year}\n"
            )


def read_from_file(filename):
    objects = []

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            data = line.strip().split("|")

            if len(data) == 4:
                name = data[0]
                source = data[1]
                location = data[2]
                year = int(data[3])

                objects.append(
                    GameObject(name, source, location, year)
                )

    return objects


print("SHORELINE TOTTORI")
print("Робота з файловими даними")
print()

objects = []

number = int(input("Введіть кількість об'єктів: "))

for i in range(number):
    print(f"\nОб'єкт {i + 1}")

    name = input("Назва об'єкта: ")
    source = input("Джерело інформації: ")
    location = input("Місце розташування: ")
    year = int(input("Рік: "))

    objects.append(
        GameObject(name, source, location, year)
    )

filename = "shoreline_tottori.txt"

save_to_file(objects, filename)

print("\nДані успішно записано у файл.")

loaded_objects = read_from_file(filename)

print("\nОб'єкти, пов'язані з набережною Tottori:")
print("-" * 60)

found = False

for obj in loaded_objects:
    if "Tottori" in obj.location or "набереж" in obj.location.lower():
        print(f"Назва: {obj.name}")
        print(f"Джерело: {obj.source}")
        print(f"Місце: {obj.location}")
        print(f"Рік: {obj.year}")
        print("-" * 60)
        found = True

if not found:
    print("Об'єктів за заданою умовою не знайдено.")