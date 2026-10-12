# -*- coding: utf-8 -*-
"""
ЛР №2 (ООП): розгалужені та циклічні програми. Мова: Python.
Варіант 1 (завдання 1, 2, 3 — перші рядки таблиць із методички).
Адаптовано до курсової "Shoreline Tottori" (узбережжя Тотторі, ООП).

Ігрова інтерпретація:
  Завдання 1 — модифікатор прибою залежно від рівня припливу x.
  Завдання 2 — затухання шуму хвиль залежно від відстані x від берега.
  Завдання 3 — рівень розкриття історії залежно від прогресу гравця y.
"""
import math


def read_float(prompt):
    """Зчитує дійсне число; приймає і кому, і крапку."""
    while True:
        try:
            return float(input(prompt).replace(",", "."))
        except ValueError:
            print("  Помилка: введіть число.")


def print_table(rows, head_x, head_y):
    """Таблиця: № точки | аргумент | значення функції."""
    print(f"\n{'№':>3} | {head_x:>10} | {head_y:>12}")
    print("-" * 32)
    for n, x, y in rows:
        val = f"{y:12.5f}" if y is not None else f"{'немає':>12}"
        print(f"{n:>3} | {x:10.3f} | {val}")


# ---------- ООП-частина: «природні явища» узбережжя ----------
class CoastFunction:
    """Базовий клас: одна функція з гри + її область визначення."""
    name = ""

    def value(self, arg):
        raise NotImplementedError


class TideSurf(CoastFunction):
    """Завдання 1. y(x): x — рівень припливу, y — модифікатор прибою.
       -cos^2(x-pi),   -pi < x < pi/4
       sqrt(|x+1|),    pi/4 <= x <= 1
       1/(x-1),        x > 1
    """
    name = "Прибій (приплив)"

    def value(self, x):
        if -math.pi < x < math.pi / 4:
            return -math.cos(x - math.pi) ** 2
        elif math.pi / 4 <= x <= 1:
            return math.sqrt(abs(x + 1))
        elif x > 1:
            return 1 / (x - 1)
        return None  # x <= -pi: поза областю визначення


class WaveNoise(CoastFunction):
    """Завдання 2. y = cos^2(x) / (x^2 + 1); x — відстань від берега."""
    name = "Шум хвиль"

    def value(self, x):
        return math.cos(x) ** 2 / (x ** 2 + 1)


class StoryReveal(CoastFunction):
    """Завдання 3. w(y): y — прогрес гравця (знайдені підказки/етапи).
       y + sin y,            -6.5 < y < 0.5
       ln(y + cbrt(y)),      0.5 <= y <= 8
    """
    name = "Розкриття історії"

    def value(self, y):
        if -6.5 < y < 0.5:
            return y + math.sin(y)
        elif 0.5 <= y <= 8:
            return math.log(y + y ** (1 / 3))
        return None


# ---------- Завдання 1 ----------
def task1():
    f = TideSurf()
    x = read_float("Рівень припливу x: ")
    y = f.value(x)
    if y is None:
        print("x ≤ -π: поза областю визначення функції.")
    else:
        branch = ("-cos²(x-π)" if x < math.pi / 4
                  else "√|x+1|" if x <= 1 else "1/(x-1)")
        print(f"Гілка: {branch}\nМодифікатор прибою y({x}) = {y:.5f}")


# ---------- Завдання 2: версія 1 — з «goto» ----------
def task2_goto():
    """У Python немає goto. Його імітує автомат станів: кожне значення
    state — це «мітка», а присвоєння state = '...' — це «goto мітка»."""
    f = WaveNoise()
    a = read_float("Початкова відстань a: ")
    b = read_float("Кінцева відстань b: ")
    h = read_float("Крок h: ")
    rows, n, state = [], 0, "check"
    while True:
        if state == "check":  # мітка check:
            x = a + n * h
            state = "body" if x <= b + 1e-9 else "end"  # if ... goto
        elif state == "body":  # мітка body:
            rows.append((n + 1, x, f.value(x)))
            n += 1
            state = "check"  # goto check
        elif state == "end":  # мітка end:
            break
    print_table(rows, "x", "y")


# ---------- Завдання 2: версія 2 — з циклом ----------
def task2_loop():
    f = WaveNoise()
    a = read_float("Початкова відстань a: ")
    b = read_float("Кінцева відстань b: ")
    h = read_float("Крок h: ")
    rows, n = [], 0
    while a + n * h <= b + 1e-9:  # n*h замість x+=h: без накопичення похибки
        x = a + n * h
        rows.append((n + 1, x, f.value(x)))
        n += 1
    print_table(rows, "x", "y")


# ---------- Завдання 3 ----------
def task3():
    f = StoryReveal()
    lo = read_float("Нижня межа (за варіантом -6.5): ")
    hi = read_float("Верхня межа (за варіантом 8): ")
    y0 = read_float("Початкове значення y: ")
    h = read_float("Крок Δy: ")
    rows, n = [], 0
    while y0 + n * h <= hi + 1e-9:
        y = y0 + n * h
        # значення поза межами області визначення -> None («немає»)
        w = f.value(y) if lo <= y <= hi else None
        rows.append((n + 1, y, w))
        n += 1
    print_table(rows, "y", "w")


def main():
    menu = {"1": ("Завдання 1: прибій", task1),
            "2": ("Завдання 2 (goto)", task2_goto),
            "3": ("Завдання 2 (цикл)", task2_loop),
            "4": ("Завдання 3: історія", task3)}
    while True:
        print("\n=== Shoreline Tottori: ЛР №2 ===")
        for k, (t, _) in menu.items():
            print(f"{k} — {t}")
        print("0 — вихід")
        c = input("Вибір: ").strip()
        if c == "0":
            break
        if c in menu:
            menu[c][1]()
        else:
            print("Невірний пункт меню.")


if __name__ == "__main__":
    main()