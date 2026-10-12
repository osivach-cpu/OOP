class GameTime:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self._check_time()

    def _check_time(self):
        if not (0 <= self.hours < 24):
            raise ValueError("Години повинні бути від 0 до 23.")
        if not (0 <= self.minutes < 60):
            raise ValueError("Хвилини повинні бути від 0 до 59.")
        if not (0 <= self.seconds < 60):
            raise ValueError("Секунди повинні бути від 0 до 59.")

    def input_time(self):
        while True:
            try:
                self.hours = int(input("Введіть години (0-23): "))
                self.minutes = int(input("Введіть хвилини (0-59): "))
                self.seconds = int(input("Введіть секунди (0-59): "))

                self._check_time()
                break
            except ValueError:
                print("Помилка! Введіть коректний час.")

    def show_time(self):
        print(f"Ігровий час: {self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}")

    def seconds_from_start(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def time_to_end(self):
        total_seconds = 24 * 60 * 60 - self.seconds_from_start()

        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60

        print(
            f"До завершення доби залишилось: "
            f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        )

    def __add__(self, seconds):
        total = self.seconds_from_start() + seconds
        total %= 24 * 60 * 60

        hours = total // 3600
        minutes = (total % 3600) // 60
        seconds = total % 60

        return GameTime(hours, minutes, seconds)

    def __sub__(self, seconds):
        total = self.seconds_from_start() - seconds
        total %= 24 * 60 * 60

        hours = total // 3600
        minutes = (total % 3600) // 60
        seconds = total % 60

        return GameTime(hours, minutes, seconds)

    def __del__(self):
        print("Об'єкт GameTime знищено.")


print()
print("       SHORELINE TOTTORI")
print("       Система ігрового часу")
print()

game_time = GameTime()

print("\nВведіть початковий ігровий час:")
game_time.input_time()

print("\nПочатковий стан:")
game_time.show_time()
game_time.time_to_end()

while True:
    print("\nОберіть дію:")
    print("1 - Додати час")
    print("2 - Відняти час")
    print("3 - Показати поточний час")
    print("4 - Показати час до завершення доби")
    print("0 - Завершити програму")

    choice = input("Ваш вибір: ")

    if choice == "1":
        try:
            seconds = int(input("Скільки секунд додати: "))
            game_time = game_time + seconds

            print("\nПісля додавання часу:")
            game_time.show_time()

        except ValueError:
            print("Помилка! Введіть ціле число.")

    elif choice == "2":
        try:
            seconds = int(input("Скільки секунд відняти: "))
            game_time = game_time - seconds

            print("\nПісля віднімання часу:")
            game_time.show_time()

        except ValueError:
            print("Помилка! Введіть ціле число.")

    elif choice == "3":
        game_time.show_time()

    elif choice == "4":
        game_time.time_to_end()

    elif choice == "0":
        print("\nПрограму завершено.")
        break

    else:
        print("Невірний вибір. Спробуйте ще раз.")