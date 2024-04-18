def weekend_or_working_day(day: str):
    working_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    weekend_days = ['Saturday', 'Sunday']

    if day in working_days:
        return 'Working day'

    elif day in weekend_days:
        return 'Weekend'

    else:
        return 'Error'


day_of_week = input()
print(weekend_or_working_day(day_of_week))
