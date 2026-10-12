print("SHORELINE TOTTORI")
print("Оцінка стану об'єктів ігрової локації")
print()

grades = list(map(int, input(
    "Введіть оцінки об'єктів через пробіл: "
).split()))

text_grades = []

for grade in grades:
    if grade == 5:
        text_grades.append("відмінно")
    elif grade == 4:
        text_grades.append("добре")
    elif grade == 3:
        text_grades.append("задовільно")
    elif grade == 2:
        text_grades.append("незадовільно")
    elif grade == 1:
        text_grades.append("дуже погано")
    else:
        text_grades.append("невідома оцінка")

print()
print("Числовий масив оцінок:")
print(grades)

print()
print("Текстовий масив оцінок:")
print(text_grades)