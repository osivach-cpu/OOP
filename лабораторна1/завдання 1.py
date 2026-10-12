import math

class verificationofthedomain:

    EPS = 1e-9

    def __init__(self):
        self.two_pi = 2 * math.pi

    def verificationX(self, x: float):

        arg_log = x + self.two_pi
        if arg_log <= 0:
            return False, "ой-ой X поза ОДЗ, спрабуй ще"

        if abs(arg_log - 1) < self.EPS:
            return False, "ой-ой X поза ОДЗ, спрабуй ще"

        under_root = math.sin(x + 1) + math.atan(math.pi * x)
        if under_root < -self.EPS:
            return False, "ой-ой X поза ОДЗ, спрабуй ще"

        return True,""

    def calculateX(self, x: float):

        ok, reason = self.verificationX(x)
        if not ok:
            return None, reason

        try:
            under_root = math.sin(x + 1) + math.atan(math.pi * x)
            numerator = math.sqrt(under_root)
            denominator = math.log10(x + self.two_pi)
            y = numerator / denominator - 1
            return y, None
        except (ValueError, ZeroDivisionError) as e:
            return None, f"обчислювальна помилка: {e}"
class user:

    @staticmethod
    def reader(prompt: str):

        raw = input(prompt).strip()
        try:
            return float(raw)
        except ValueError:
            return None

def main():
    solver = verificationofthedomain()

    while True:
        raw = input("Введіть значення x: ").strip()

        if raw.lower() in ("exit", "quit", "вихід"):
            print("Завершення роботи.")
            break

        try:
            x = float(raw)
        except ValueError:
            print("ні-ні-ні мені потрібні числа а не текст)\n")
            continue

        y, error = solver.calculateX(x)

        if error is not None:
            print(f"{error}\n")
        else:
            print(f"y({x}) = {y:.6f}\n")

if __name__ == "__main__":
    main()


