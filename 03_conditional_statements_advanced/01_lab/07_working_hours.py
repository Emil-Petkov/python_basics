def working_hours(hour: int, day_of_week: str):
    working_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', ]

    if day_of_week in working_days and 10 <= hour <= 18:
        return 'open'

    return 'closed'


hour = int(input())
day_of_week = input()
print(working_hours(hour, day_of_week))
