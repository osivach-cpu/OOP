import random

class CoastMap:
    ZONES = 6
    CELLS = 7

    def __init__(self):
        self.grid = [
            [random.randint(0, 9) for _ in range(self.CELLS)]
            for _ in range(self.ZONES)
        ]

    def show(self, title):
        print(title)
        for number, row in enumerate(self.grid, start=1):
            print(f"Зона {number}:", *row)
        print()

    def put_strongest_first(self):
        for row in self.grid:
            index = row.index(max(row))
            row[0], row[index] = row[index], row[0]

    def ask_zone(self):
        while True:
            text = input(f"Яку зону оглянути? (1-{self.ZONES}, 0 - вийти): ").strip()
            if text.isdigit() and 0 <= int(text) <= self.ZONES:
                return int(text)
            print("Некоректне значення. Спробуйте ще раз.")

    def inspect_zone(self, zone):
        row = self.grid[zone - 1]
        print(f"Зона {zone}: найпомітніша підказка - {row[0]}; усі клітинки:", *row)


if __name__ == "__main__":
    coast = CoastMap()
    coast.show("Карта узбережжя до перетворення:")
    coast.put_strongest_first()
    coast.show("Карта узбережжя після перетворення:")

    while True:
        zone = coast.ask_zone()
        if zone == 0:
            break
        coast.inspect_zone(zone)