import math


def area_of_figures(figure: str):
    if figure == 'square':
        side = float(input())

        return side * side

    elif figure == 'rectangle':
        side_a = float(input())
        side_b = float(input())

        return side_a * side_b

    elif figure == 'circle':
        radius = float(input())

        return radius * radius * math.pi

    elif figure == 'triangle':
        side = float(input())
        height = float(input())

        return side * height / 2


figures = input()
print(f'{area_of_figures(figures):.3f}')
