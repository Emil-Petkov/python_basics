import math

type_figure = input()

if type_figure == 'square':
    side = float(input())
    area = side ** 2
    print(f'{area:.3f}')

elif type_figure == 'rectangle':
    side_a = float(input())
    side_b = float(input())
    area = side_a * side_b
    print(f'{area:.3f}')

elif type_figure == 'circle':
    radius = float(input())
    area = math.pi * radius ** 2
    print(f'{area:.3f}')

elif type_figure == 'triangle':
    length = float(input())
    height = float(input())
    area = length * height / 2
    print(f'{area:.3f}')
