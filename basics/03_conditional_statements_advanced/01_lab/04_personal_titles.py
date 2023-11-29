age = float(input())
gander = input()

if gander == 'm':
    if age < 16:
        print('Master')

    else:
        print('Mr.')

elif gander == 'f':
    if age < 16:
        print('Miss')

    else:
        print('Ms.')
