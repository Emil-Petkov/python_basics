length = int(input())
width = int(input())
height = int(input())
percent = float(input())

tank_area_in_q3cm = length * width * height
needed_liters = tank_area_in_q3cm / 1000

free_space = needed_liters - (needed_liters * (percent / 100))

print(free_space)
