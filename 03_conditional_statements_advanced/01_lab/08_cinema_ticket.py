def cinema_ticket(day: str):
    price = {
        'Monday': 12,
        'Tuesday': 12,
        'Wednesday': 14,
        'Thursday': 14,
        'Friday': 12,
        'Saturday': 16,
        'Sunday': 16,
    }

    if day in price:
        return price[day]


day_of_week = input()
print(cinema_ticket(day_of_week))
