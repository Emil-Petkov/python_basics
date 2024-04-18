def triangle_area(side: float, height: float):
    area = (side * height) / 2

    return f'{area:.2f}'


side = float(input())
height = float(input())
print(triangle_area(side, height))
