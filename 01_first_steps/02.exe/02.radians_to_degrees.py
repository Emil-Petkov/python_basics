import math


def radians_to_degrees(radians: float):
    calculate = (radians * 180) / math.pi

    return calculate


radian = float(input())
print(radians_to_degrees(radian))
