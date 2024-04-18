import math


def circle_area_and_perimeter(radius: float):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius

    return f'{area:.2f}\n{circumference:.2f}'


circus_radius = float(input())
print(circle_area_and_perimeter(circus_radius))
