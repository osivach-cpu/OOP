class Progression:
    def __init__(self, first=0):
        self.first = first

    def nth_element(self, n):
        return self.first

    def sum_elements(self, n):
        return self.first * n

    def show_info(self):
        print("Перший член прогресії:", self.first)


class ArithmeticProgression(Progression):
    def __init__(self, first=0, difference=0):
        super().__init__(first)
        self.difference = difference

    def nth_element(self, n):
        return self.first + (n - 1) * self.difference

    def sum_elements(self, n):
        return n * (2 * self.first + (n - 1) * self.difference) / 2

    def show_info(self):
        print("Тип: Арифметична прогресія")
        print("Перша нагорода:", self.first)
        print("Збільшення нагороди:", self.difference)


class GeometricProgression(Progression):
    def __init__(self, first=0, ratio=1):
        super().__init__(first)
        self.ratio = ratio

    def nth_element(self, n):
        return self.first * self.ratio ** (n - 1)

    def sum_elements(self, n):
        if self.ratio == 1:
            return self.first * n
        return self.first * (self.ratio ** n - 1) / (self.ratio - 1)

    def show_info(self):
        print("Тип: Геометрична прогресія")
        print("Перша нагорода:", self.first)
        print("Множник нагороди:", self.ratio)


class Game:
    def __init__(self):
        self.progressions = []

    def add_progression(self):
        print("\nДодавання системи нагород")
        print("1 - Арифметична прогресія")
        print("2 - Геометрична прогресія")

        choice = input("Оберіть тип: ")

        try:
            first = float(input("Введіть нагороду за перше завдання: "))

            if choice == "1":
                difference = float(
                    input("Введіть збільшення нагороди: ")
                )
                progression = ArithmeticProgression(
                    first, difference
                )
                self.progressions.append(progression)
                print("Арифметичну систему нагород додано.")

            elif choice == "2":
                ratio = float(
                    input("Введіть множник нагороди: ")
                )

                if ratio == 0:
                    print("Множник не може дорівнювати 0.")
                    return

                progression = GeometricProgression(
                    first, ratio
                )
                self.progressions.append(progression)
                print("Геометричну систему нагород додано.")

            else:
                print("Неправильний вибір.")

        except ValueError:
            print("Помилка! Введіть числове значення.")

    def show_progressions(self):
        if not self.progressions:
            print("\nСписок систем нагород порожній.")
            return

        print("\n--- Системи нагород Shoreline Tottori ---")

        for i, progression in enumerate(self.progressions, 1):
            print(f"\nСистема №{i}")
            progression.show_info()

    def calculate_nth(self):
        if not self.progressions:
            print("\nСписок систем нагород порожній.")
            return

        try:
            number = int(
                input("Введіть номер системи: ")
            )

            if number < 1 or number > len(self.progressions):
                print("Такої системи немає.")
                return

            n = int(
                input("Введіть номер сюжетного завдання: ")
            )

            if n <= 0:
                print("Номер завдання повинен бути додатним.")
                return

            result = self.progressions[number - 1].nth_element(n)

            print(
                f"Нагорода за завдання №{n}: {result:.2f}"
            )

        except ValueError:
            print("Помилка! Введіть ціле число.")

    def calculate_sum(self):
        if not self.progressions:
            print("\nСписок систем нагород порожній.")
            return

        try:
            number = int(
                input("Введіть номер системи: ")
            )

            if number < 1 or number > len(self.progressions):
                print("Такої системи немає.")
                return

            n = int(
                input("Введіть кількість виконаних завдань: ")
            )

            if n <= 0:
                print("Кількість завдань повинна бути додатною.")
                return

            result = self.progressions[number - 1].sum_elements(n)

            print(
                f"Загальна нагорода за {n} завдань: "
                f"{result:.2f}"
            )

        except ValueError:
            print("Помилка! Введіть ціле число.")

    def search(self):
        if not self.progressions:
            print("\nСписок систем нагород порожній.")
            return

        try:
            value = float(
                input("Введіть першу нагороду для пошуку: ")
            )

            found = False

            for i, progression in enumerate(
                self.progressions, 1
            ):
                if progression.first == value:
                    print(
                        f"\nЗнайдено систему №{i}"
                    )
                    progression.show_info()
                    found = True

            if not found:
                print("Систему з такою нагородою не знайдено.")

        except ValueError:
            print("Помилка! Введіть число.")

    def edit(self):
        if not self.progressions:
            print("\nСписок систем нагород порожній.")
            return

        try:
            number = int(
                input("Введіть номер системи для редагування: ")
            )

            if number < 1 or number > len(self.progressions):
                print("Такої системи немає.")
                return

            progression = self.progressions[number - 1]

            print("\nВведіть нові дані.")

            progression.first = float(
                input("Нова нагорода за перше завдання: ")
            )

            if isinstance(progression, ArithmeticProgression):
                progression.difference = float(
                    input("Нове збільшення нагороди: ")
                )

            elif isinstance(progression, GeometricProgression):
                progression.ratio = float(
                    input("Новий множник нагороди: ")
                )

            print("Запис успішно відредаговано.")

        except ValueError:
            print("Помилка! Введіть правильне числове значення.")

    def start(self):
        while True:
            print()
            print("       SHORELINE TOTTORI")
            print()
            print("1 - Додати систему нагород")
            print("2 - Переглянути системи нагород")
            print("3 - Знайти систему")
            print("4 - Розрахувати нагороду за завдання")
            print("5 - Розрахувати загальну нагороду")
            print("6 - Редагувати систему")
            print("0 - Вихід")

            choice = input("Оберіть дію: ")

            if choice == "1":
                self.add_progression()

            elif choice == "2":
                self.show_progressions()

            elif choice == "3":
                self.search()

            elif choice == "4":
                self.calculate_nth()

            elif choice == "5":
                self.calculate_sum()

            elif choice == "6":
                self.edit()

            elif choice == "0":
                print("Програму завершено.")
                break

            else:
                print("Неправильний вибір.")


game = Game()
game.start()