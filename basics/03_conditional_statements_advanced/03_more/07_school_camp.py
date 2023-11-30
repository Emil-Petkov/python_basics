season_of_year = input()
type_of_group = input()
number_of_students = int(input())
days = int(input())

needed_money = 0
type_sport = ''

if season_of_year == 'Winter':
    if type_of_group in ['boys', 'girls']:
        needed_money += (number_of_students * 9.60) * days

        if type_of_group == 'boys':
            type_sport = 'Judo'

        else:
            type_sport = 'Gymnastics'

    elif type_of_group == 'mixed':
        needed_money += (number_of_students * 10.00) * days
        type_sport = 'Ski'

elif season_of_year == 'Spring':
    if type_of_group in ['boys', 'girls']:
        needed_money += (number_of_students * 7.20) * days

        if type_of_group == 'boys':
            type_sport = 'Tennis'

        else:
            type_sport = 'Athletics'

    elif type_of_group == 'mixed':
        needed_money += (number_of_students * 9.50) * days
        type_sport = 'Cycling'

elif season_of_year == 'Summer':
    if type_of_group in ['boys', 'girls']:
        needed_money += (number_of_students * 15.00) * days

        if type_of_group == 'boys':
            type_sport = 'Football'

        else:
            type_sport = 'Volleyball'

    elif type_of_group == 'mixed':
        needed_money += (number_of_students * 20.00) * days
        type_sport = 'Swimming'

if number_of_students >= 50:
    needed_money -= needed_money * 0.50

elif 20 <= number_of_students < 50:
    needed_money -= needed_money * 0.15

elif 10 <= number_of_students < 20:
    needed_money -= needed_money * 0.05

print(f'{type_sport} {needed_money:.2f} lv.')
