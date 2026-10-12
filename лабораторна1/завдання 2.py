import math
class Mistake(Exception):
    pass
class Calculator:

    GAMMA = -3.41
    EPS = 1e-9

    def __init__(self, gamma: float = GAMMA):
        self.gamma = gamma

    @staticmethod
    def cube_root(value: float) -> float:

        if value < 0:
            return -((-value) ** (1.0 / 3.0))
        return value ** (1.0 / 3.0)

    def compute_y(self, x: float) -> float:

        cos_val = math.cos(x - 1)
        if abs(cos_val) < self.EPS:
            raise Mistake("ой-ой-ой розв'язку немає(")
        tan_val = math.tan(x - 1)
        return tan_val ** 4

    def compute_new_x(self, y: float) -> float:

        arg = abs(y + 6)
        if arg < self.EPS:
            raise Mistake("ой-ой-ой розв'язку немає(")
        return math.log10(arg) + 0.77

    def compute_a(self, x: float, y: float) -> float:

        root_part = self.cube_root(y + 0.01)
        sin_part = math.sin(math.pi * x) ** 2
        return self.gamma * root_part + sin_part

    def solve(self, x0: float) -> float:

        y = self.compute_y(x0)
        x_new = self.compute_new_x(y)
        a = self.compute_a(x_new, y)
        return a


def read_float(prompt: str) -> float:

    while True:
        raw = input(prompt).strip().replace(",", ".")
        try:
            return float(raw)
        except ValueError:
            print("так-так-так потрібне дійсне число")


def main():
    calculator = Calculator(gamma=-3.41)

    x0 = read_float("який бажаєте x?: ")

    try:
        result = calculator.solve(x0)
    except Mistake as e:
        print(f"ой-ой-ой розв'язку немає( спробуй ще")
        return
    except (ValueError, OverflowError, ZeroDivisionError):
        print(f"ой-ой-ой розв'язку немає( спробуй ще")
        return

    print(f"y = {calculator.compute_y(x0):.6f}")
    print(f"нове x = {calculator.compute_new_x(calculator.compute_y(x0)):.6f}")
    print(f"a = {result:.6f}")


if __name__ == "__main__":
    main()