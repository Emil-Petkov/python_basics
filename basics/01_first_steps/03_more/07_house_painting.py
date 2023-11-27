height_house = float(input())
length_wall = float(input())
height_triangle = float(input())

front_wall = height_house * height_house - (2 * 1.2)
back_wall = height_house * height_house
front_and_back_wall = front_wall + back_wall

side_walls = 2 * (height_house * length_wall) - (2 * (1.5 * 1.5))

total_area_walls = front_and_back_wall + side_walls

needed_green_paint = total_area_walls / 3.4

################################################################

front_and_back_side_roof = (height_house * height_triangle / 2) * 2
side_roof = (length_wall * height_house) * 2

total_area_roof = front_and_back_side_roof + side_roof

needed_red_paint = total_area_roof / 4.3

print(f'{needed_green_paint:.2f}')
print(f'{needed_red_paint:.2f}')
