def ski_trip(days: int, room_type: str, grade: str):
    total = 0
    total_nights = days - 1

    price_per_rooms = {
        'room for one person': 18.00,
        'apartment': 25.00,
        'president apartment': 35.00,
    }

    if room_type == 'apartment':
        if days < 10:
            total = (price_per_rooms[room_type] * total_nights) * 0.70  # 30% discount

        elif days <= 15:
            total = (price_per_rooms[room_type] * total_nights) * 0.65

        else:
            total = (price_per_rooms[room_type] * total_nights) * 0.50

    elif room_type == 'president apartment':
        if days < 10:
            total = (price_per_rooms[room_type] * total_nights) * 0.90

        elif days <= 15:
            total = (price_per_rooms[room_type] * total_nights) * 0.85

        else:
            total = (price_per_rooms[room_type] * total_nights) * 0.80

    elif room_type == 'room for one person':
        total = price_per_rooms[room_type] * total_nights

    if grade == 'positive':
        total *= 1.25

    elif grade == 'negative':
        total -= total * 0.10

    return f'{total:.2f}'


days = int(input())
room_type = input()
grade = input()
print(ski_trip(days, room_type, grade))
