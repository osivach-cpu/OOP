import random

class ShorelineSurvey:

    MIN_SECTORS = 4

    def __init__(self):
        self.sector_count = 0
        self.clues = []
        self.even_clues = []
    def ask_sector_count(self):
        while True:
            text = input("Введіть кількість секторів узбережжя (ціле число більше 3): ").strip()
            if text.isdigit() and int(text) >= self.MIN_SECTORS:
                self.sector_count = int(text)
                return
            print("Некоректне значення. Потрібне натуральне число більше 3. Спробуйте ще раз.")

    def generate_clues(self):
        n = self.sector_count
        self.clues = [random.randint(0, n) for _ in range(n)]

    def select_even(self):
        self.even_clues = [value for value in self.clues if value % 2 == 0]

    def show(self):
        print("\nПідказки за секторами:", *self.clues)
        if self.even_clues:
            print("Сектори з парною кількістю підказок:", *self.even_clues)
        else:
            print("Парних значень у масиві немає.")


if __name__ == "__main__":
    survey = ShorelineSurvey()
    survey.ask_sector_count()
    survey.generate_clues()
    survey.select_even()
    survey.show()