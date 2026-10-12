class Student:
    def __init__(self, surname, group, grades):
        self.surname = surname
        self.group = group
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)

    def has_only_4_or_5(self):
        return all(grade == 4 or grade == 5 for grade in self.grades)

    def show(self):
        print(
            self.surname,
            "| група:", self.group,
            "| оцінки:", self.grades,
            "| середній бал:", round(self.average(), 2)
        )


print("SHORELINE TOTTORI")
print("Обробка даних персонажів ігрової системи")
print()

n = int(input("Введіть кількість записів: "))

students = []

for i in range(n):
    print()
    print("Запис", i + 1)

    surname = input("Введіть прізвище та ініціали: ")
    group = input("Введіть номер групи: ")

    grades = []

    print("Введіть 5 оцінок:")

    for j in range(5):
        grade = int(input("Оцінка " + str(j + 1) + ": "))
        grades.append(grade)

    students.append(Student(surname, group, grades))


students.sort(key=lambda student: student.average())

print()
print("Записи за зростанням середнього бала:")

for student in students:
    student.show()


print()
print("Студенти, які мають тільки оцінки 4 або 5:")

found = False

for student in students:
    if student.has_only_4_or_5():
        print("Прізвище:", student.surname,
              "| Група:", student.group)
        found = True

if not found:
    print("Таких студентів немає.")