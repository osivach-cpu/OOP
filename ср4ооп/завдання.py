class ShorelineTottori:
    def __init__(self, array):
        self.array = array

    def show_all(self):
        for element in self.array:
            print(element)

    def show_reverse(self):
        for i in range(len(self.array) - 1, -1, -1):
            print(self.array[i])

    def show_even(self):
        for element in self.array:
            if element % 2 == 0:
                print(element)

    def show_every_second(self):
        for i in range(0, len(self.array), 2):
            print(self.array[i])

    def show_until_minus_one(self):
        for element in self.array:
            if element == -1:
                break
            print(element)

    def add_to_end(self, value):
        self.array.append(value)

    def add_to_beginning(self, value):
        self.array.insert(0, value)

    def add_at_position(self, value, position):
        self.array.insert(position, value)

    def delete_from_end(self):
        if len(self.array) > 0:
            self.array.pop()

    def delete_from_beginning(self):
        if len(self.array) > 0:
            self.array.pop(0)

    def delete_at_position(self, position):
        if 0 <= position < len(self.array):
            self.array.pop(position)
        else:
            print("Такої позиції немає.")

    def merge_arrays(self, second_array):
        return self.array + second_array


def input_number(text):
    while True:
        value = input(text)

        try:
            return int(value)
        except ValueError:
            print("Попередження: введіть число.")


array = []

print("SHORELINE TOTTORI")
print("Введення об'єктів узбережжя")

n = input_number("Введіть кількість елементів масиву: ")

for i in range(n):
    value = input_number(f"Введіть елемент {i + 1}: ")
    array.append(value)

shoreline = ShorelineTottori(array)

print("\nПочатковий масив:")
print(shoreline.array)

print("\nБлок 1. Усі елементи:")
shoreline.show_all()

print("\nБлок 2. У зворотному порядку:")
shoreline.show_reverse()

print("\nБлок 3. Парні елементи:")
shoreline.show_even()

print("\nБлок 4. Елементи через 1:")
shoreline.show_every_second()

print("\nБлок 5. До елемента -1:")
shoreline.show_until_minus_one()

print("\n--- Додавання і видалення ---")

value = input_number("Додати елемент у кінець: ")
shoreline.add_to_end(value)
print("Масив:", shoreline.array)

value = input_number("Додати елемент на початок: ")
shoreline.add_to_beginning(value)
print("Масив:", shoreline.array)

value = input_number("Додати елемент у позицію 4: ")
shoreline.add_at_position(value, 4)
print("Масив:", shoreline.array)

shoreline.delete_from_end()
print("Після видалення з кінця:", shoreline.array)

shoreline.delete_from_beginning()
print("Після видалення з початку:", shoreline.array)

shoreline.delete_at_position(5)
print("Після видалення елемента з позиції 5:", shoreline.array)

print("\n--- Об'єднання двох масивів ---")

second_array = []

n = input_number("Введіть кількість елементів другого масиву: ")

for i in range(n):
    value = input_number(f"Введіть елемент {i + 1}: ")
    second_array.append(value)

result = shoreline.merge_arrays(second_array)

print("Перший масив:", shoreline.array)
print("Другий масив:", second_array)
print("Об'єднаний масив:", result)