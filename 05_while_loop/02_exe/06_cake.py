width_cake = int(input())
height_cake = int(input())

total_pieces = width_cake * height_cake

while not total_pieces <= 0:
    command = input()

    if command == 'STOP':
        print(f'{total_pieces} pieces are left.')
        exit()

    else:
        total_pieces -= int(command)

print(f'No more cake left! You need {abs(total_pieces)} pieces more.')
