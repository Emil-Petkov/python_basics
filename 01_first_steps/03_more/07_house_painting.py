def house_painting(height_house, length_side, height_triangle):
    front_and_back_walls_area = (height_house * height_house) * 2
    door = 1.20 * 2.00  # cm.
    total_area_front_back_walls_minus_door = front_and_back_walls_area - door
    area_length_side_walls = (length_side * height_house) * 2
    windows_area = (1.50 * 1.50) * 2  # cm.
    total_area_side_walls = area_length_side_walls - windows_area

    green_area = total_area_front_back_walls_minus_door + total_area_side_walls

    needed_liters_green_paint = green_area / 3.4  # liters paint

    area_front_back_roolf = ((height_triangle * height_house) / 2) * 2
    area_side_roolf = (height_house * length_side) * 2

    needed_liters_red_paint = (area_front_back_roolf + area_side_roolf) / 4.3  # liters paint

    return f'{needed_liters_green_paint:.2f}\n{needed_liters_red_paint:.2f}'


height_house = float(input())
length_side = float(input())
height_triangle = float(input())
print(house_painting(height_house, length_side, height_triangle))
