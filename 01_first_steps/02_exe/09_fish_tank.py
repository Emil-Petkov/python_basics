def fish_tank(length: int, width: int, height: int, percent: float):
    area_in_cubic_meter = length * width * height
    area_in_liters = area_in_cubic_meter / 1000

    free_space_in_liters = area_in_liters * (1 - (percent / 100))

    return free_space_in_liters


length_in_cm = int(input())
width_in_cm = int(input())
height_in_cm = int(input())
percentage = float(input())
print(fish_tank(length_in_cm, width_in_cm, height_in_cm, percentage))
