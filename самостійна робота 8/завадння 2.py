import math
class Polygon:
    def __init__(self, points):
        self.points = points

    def perimeter(self):
        result = 0

        for i in range(len(self.points)):
            x1, y1 = self.points[i]
            x2, y2 = self.points[(i + 1) % len(self.points)]

            result += math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        return result

    def area(self):
        result = 0

        for i in range(len(self.points)):
            x1, y1 = self.points[i]
            x2, y2 = self.points[(i + 1) % len(self.points)]

            result += x1 * y2 - x2 * y1

        return abs(result) / 2

    def median_point(self):
        x = sum(point[0] for point in self.points) / len(self.points)
        y = sum(point[1] for point in self.points) / len(self.points)

        return x, y

    def get_state(self):
        return {
            "Кількість вершин": len(self.points),
            "Площа": self.area(),
            "Периметр": self.perimeter(),
            "Точка перетину медіан": self.median_point()
        }


print("SHORELINE TOTTORI")
print("Створення багатокутника ігрової локації")
print()

n = int(input("Введіть кількість вершин багатокутника: "))

points = []

for i in range(n):
    print()
    print("Вершина", i + 1)

    x = float(input("x = "))
    y = float(input("y = "))

    points.append((x, y))

polygon = Polygon(points)

print()
print("Стан об'єкта:")

state = polygon.get_state()

for key, value in state.items():
    print(key + ":", value)