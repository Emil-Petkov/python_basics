width = int(input())
length = int(input())
height = int(input())

total_space = width * length * height

while not total_space <= 0:
    command = input()

    if command == 'Done':
        print(f'{total_space} Cubic meters left.')
        exit()

    total_space -= int(command)

print(f'No more free space! You need {abs(total_space)} Cubic meters more.')
