import math


def area_of_figures(figure: str):
    area = 0

    if figure == 'square':
        side = float(input())
        area += side * side

    elif figure == 'rectangle':
        side_a = float(input())
        side_b = float(input())
        area += side_a * side_b

    elif figure == 'triangle':
        side = float(input())
        height = float(input())

        area += side * height / 2

    elif figure == 'circle':
        radius = float(input())
        area += math.pi * radius ** 2

    return f'{area:.3f}'


current_figure = input()
print(area_of_figures(current_figure))
