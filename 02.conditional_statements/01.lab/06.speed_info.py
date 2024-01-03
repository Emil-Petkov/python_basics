def speed_info(speed: float):
    if speed <= 10:
        return 'slow'

    elif 10 < speed <= 50:
        return 'average'

    elif 50 < speed <= 150:
        return 'fast'

    elif 150 < speed <= 1000:
        return 'ultra fast'

    else:
        return 'extremely fast'


speed = float(input())
print(speed_info(speed))
