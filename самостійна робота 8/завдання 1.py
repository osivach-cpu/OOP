import math
class Vector3D:
    def __init__(self, x1, y1, z1, x2, y2, z2):
        self.x1 = x1
        self.y1 = y1
        self.z1 = z1
        self.x2 = x2
        self.y2 = y2
        self.z2 = z2

    def components(self):
        return (
            self.x2 - self.x1,
            self.y2 - self.y1,
            self.z2 - self.z1
        )

    def add(self, other):
        x, y, z = self.components()
        ox, oy, oz = other.components()

        return (x + ox, y + oy, z + oz)

    def subtract(self, other):
        x, y, z = self.components()
        ox, oy, oz = other.components()

        return (x - ox, y - oy, z - oz)

    def dot_product(self, other):
        x, y, z = self.components()
        ox, oy, oz = other.components()

        return x * ox + y * oy + z * oz

    def length(self):
        x, y, z = self.components()
        return math.sqrt(x ** 2 + y ** 2 + z ** 2)

    def cosine(self, other):
        product = self.dot_product(other)
        denominator = self.length() * other.length()

        if denominator == 0:
            return 0

        return product / denominator


print("SHORELINE TOTTORI")
print("Робота з векторами ігрового простору")
print()

print("Введіть координати початку першого вектора:")
x1 = float(input("x1 = "))
y1 = float(input("y1 = "))
z1 = float(input("z1 = "))

print("Введіть координати кінця першого вектора:")
x2 = float(input("x2 = "))
y2 = float(input("y2 = "))
z2 = float(input("z2 = "))

print()
print("Введіть координати початку другого вектора:")
x3 = float(input("x1 = "))
y3 = float(input("y1 = "))
z3 = float(input("z1 = "))

print("Введіть координати кінця другого вектора:")
x4 = float(input("x2 = "))
y4 = float(input("y2 = "))
z4 = float(input("z2 = "))

vector1 = Vector3D(x1, y1, z1, x2, y2, z2)
vector2 = Vector3D(x3, y3, z3, x4, y4, z4)

print()
print("Результати:")

print("Перший вектор:", vector1.components())
print("Другий вектор:", vector2.components())

print("Сума векторів:", vector1.add(vector2))
print("Різниця векторів:", vector1.subtract(vector2))

print("Скалярний добуток:", vector1.dot_product(vector2))

print("Довжина першого вектора:", vector1.length())
print("Довжина другого вектора:", vector2.length())

print("Косинус кута між векторами:", vector1.cosine(vector2))
