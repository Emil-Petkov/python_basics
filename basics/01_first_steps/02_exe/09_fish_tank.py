tank_length = int(input())
tank_width = int(input())
tank_height = int(input())
percentage = float(input())

tank_area = tank_length * tank_width * tank_height

liters = tank_area / 1000

needed_liters = liters * (1 - (percentage / 100))

print(needed_liters)
