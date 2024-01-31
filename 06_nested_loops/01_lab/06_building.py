


















floors = int(input())
rooms = int(input())

for floor in range(floors, 0, -1):

    rooms_list = []

    for room in range(rooms):
        if floor == floors:
            rooms_list.append(f'L{floor}{room}')
        elif floor % 2 == 0:
            rooms_list.append(f'O{floor}{room}')
        else:
            rooms_list.append(f'A{floor}{room}')

    print(' '.join(rooms_list))
