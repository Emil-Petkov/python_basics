def speed_info(speed: float):
    if speed <= 10:
        return 'slow'

    elif speed <= 50:
        return 'average'

    elif speed <= 150:
        return 'fast'

    elif speed <= 1000:
        return 'ultra fast'

    else:
        return 'extremely fast'


current_speed = float(input())
print(speed_info(current_speed))
