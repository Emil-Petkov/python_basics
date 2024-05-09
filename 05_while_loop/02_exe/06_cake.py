length_cake = int(input())
width_cake = int(input())
total_pieces_of_cake = length_cake * width_cake

command = input()

while not command == 'STOP':

    if int(command) < total_pieces_of_cake:
        total_pieces_of_cake -= int(command)
        command = input()
        continue

    else:
        diff = abs(int(command) - total_pieces_of_cake)
        print(f'No more cake left! You need {diff} pieces more.')

    exit()

print(f'{total_pieces_of_cake} pieces are left.')
