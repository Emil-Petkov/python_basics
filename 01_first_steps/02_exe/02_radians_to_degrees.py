import math


def radians_to_degrees(radians: float):
    result = radians * 180 / math.pi

    return result


radians = float(input())
print(radians_to_degrees(radians))
