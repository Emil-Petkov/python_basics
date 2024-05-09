width_free_space = int(input())
length_free_space = int(input())
height_free_space = int(input())

total_free_space_in_cubic_meters = width_free_space * length_free_space * height_free_space

command = input()

while command != 'Done':

    if int(command) < total_free_space_in_cubic_meters:
        total_free_space_in_cubic_meters -= int(command)
        command = input()
        continue

    else:
        diff = abs(int(command) - total_free_space_in_cubic_meters)
        print(f'No more free space! You need {diff} Cubic meters more.')
        exit()

print(f'{total_free_space_in_cubic_meters} Cubic meters left.')
