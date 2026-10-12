import math

print("Shoreline Tottori")
print("Розрахунок стану ігрової локації")
print()

z_start = float(input("Введіть початкове значення z: "))
z_end = float(input("Введіть кінцеве значення z: "))
dz = float(input("Введіть крок dz: "))

z = z_start
number = 1

print()
print(f"{'№':<5}{'z':<12}{'r':<15}")
print("-" * 32)

while z <= z_end + 0.000001:

    if -1 < z <= 0:
        r = z + math.cos(z)

    elif 0 < z <= 1:
        r = math.atan(z + math.log(z))

    else:
        print(f"{number:<5}{z:<12.2f}{'не визначено':<15}")
        z += dz
        number += 1
        continue

    print(f"{number:<5}{z:<12.2f}{r:<15.4f}")

    z += dz
    number += 1