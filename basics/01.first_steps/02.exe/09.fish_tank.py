def fish_tank(length: int, width: int, height: int, percentage: float):
    volume_in_cubic_centimeters = length * width * height
    volume_in_liters = volume_in_cubic_centimeters / 1000
    needed_liters = volume_in_liters * (1 - (percentage / 100))

    return needed_liters


length_in_centimeters = int(input())
width_in_centimeters = int(input())
height_in_centimeters = int(input())
percentage = float(input())

result = fish_tank(length_in_centimeters, width_in_centimeters, height_in_centimeters, percentage)

print(result)
