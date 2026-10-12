class GameLocation:
    def __init__(self):
        self.elements = []

    def input_array(self):
        while True:
            print("Введіть числові елементи масиву через пробіл:")

            try:
                values = input().split()
                self.elements = [float(value) for value in values]
                break
            except ValueError:
                print("Помилка! Можна вводити тільки числа.")
                print("Спробуйте ще раз.")

    def show_all(self):
        print("\nБлок 1. Усі елементи масиву:")
        for element in self.elements:
            print(element)

    def show_reverse(self):
        print("\nБлок 2. Елементи у зворотному порядку:")
        for i in range(len(self.elements) - 1, -1, -1):
            print(self.elements[i])

    def show_even(self):
        print("\nБлок 3. Парні елементи:")
        for element in self.elements:
            if element % 2 == 0:
                print(element)

    def show_every_second(self):
        print("\nБлок 4. Елементи через один:")
        for i in range(0, len(self.elements), 2):
            print(self.elements[i])

    def show_until_minus_one(self):
        print("\nБлок 5. Елементи до -1:")
        for element in self.elements:
            if element == -1:
                break
            print(element)

    def add_to_end(self):
        value = float(input("\nВведіть елемент для додавання в кінець: "))
        self.elements.append(value)

    def add_to_beginning(self):
        value = float(input("Введіть елемент для додавання на початок: "))
        self.elements.insert(0, value)

    def add_to_position(self):
        value = float(input("Введіть елемент для додавання: "))
        position = int(input("Введіть позицію: "))

        if 0 <= position <= len(self.elements):
            self.elements.insert(position, value)
        else:
            print("Такої позиції не існує.")

    def delete_from_end(self):
        if len(self.elements) > 0:
            self.elements.pop()
        else:
            print("Масив порожній.")

    def delete_from_beginning(self):
        if len(self.elements) > 0:
            self.elements.pop(0)
        else:
            print("Масив порожній.")

    def delete_from_position(self):
        position = int(input("Введіть позицію для видалення: "))

        if 0 <= position < len(self.elements):
            self.elements.pop(position)
        else:
            print("Такої позиції не існує.")

    def show_array(self):
        print("\nПоточний масив:")
        print(self.elements)


class ShorelineTottori:
    def __init__(self):
        self.location = GameLocation()

    def start(self):
        print()
        print("          SHORELINE TOTTORI")
        print("      Робота з масивами")
        print()

        self.location.input_array()

        while True:
            print("\nОберіть операцію:")
            print("1 - Вивести всі елементи")
            print("2 - Вивести у зворотному порядку")
            print("3 - Вивести парні елементи")
            print("4 - Вивести елементи через один")
            print("5 - Вивести до елемента -1")
            print("6 - Додати елемент у кінець")
            print("7 - Додати елемент на початок")
            print("8 - Додати елемент у позицію")
            print("9 - Видалити елемент з кінця")
            print("10 - Видалити елемент з початку")
            print("11 - Видалити елемент з позиції")
            print("12 - Показати поточний масив")
            print("0 - Завершити програму")

            choice = input("\nВаш вибір: ")

            if choice == "1":
                self.location.show_all()

            elif choice == "2":
                self.location.show_reverse()

            elif choice == "3":
                self.location.show_even()

            elif choice == "4":
                self.location.show_every_second()

            elif choice == "5":
                self.location.show_until_minus_one()

            elif choice == "6":
                self.location.add_to_end()

            elif choice == "7":
                self.location.add_to_beginning()

            elif choice == "8":
                self.location.add_to_position()

            elif choice == "9":
                self.location.delete_from_end()

            elif choice == "10":
                self.location.delete_from_beginning()

            elif choice == "11":
                self.location.delete_from_position()

            elif choice == "12":
                self.location.show_array()

            elif choice == "0":
                print("\nРоботу програми завершено.")
                break

            else:
                print("Неправильний вибір. Спробуйте ще раз.")


game = ShorelineTottori()
game.start()