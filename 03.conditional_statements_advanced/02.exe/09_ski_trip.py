def ski_trip(days: int, type_room: str, grade: str):
    total = 0
    overnight_stay = days - 1

    if type_room == 'room for one person':
        total = overnight_stay * 18.00

    elif type_room == 'apartment':
        total = overnight_stay * 25.00

        if overnight_stay < 10:
            total -= total * 0.30

        elif overnight_stay <= 15:
            total -= total * 0.35

        else:
            total -= total * 0.50

    elif type_room == 'president apartment':
        total = overnight_stay * 35

        if overnight_stay < 10:
            total -= total * 0.10

        elif overnight_stay <= 15:
            total -= total * 0.15

        else:
            total -= total * 0.20

    if grade == 'positive':
        total *= 1.25

    elif grade == 'negative':
        total -= total * 0.10

    return f'{total:.2f}'


days = int(input())
type_room = input()
grade = input()
print(ski_trip(days, type_room, grade))
