def trapezoid_area(a: float, b: float, h: float):
    area = (a + b) * h / 2

    return f'{area:.2f}'


side_a = float(input())
side_b = float(input())
height = float(input())
print(trapezoid_area(side_a, side_b, height))
