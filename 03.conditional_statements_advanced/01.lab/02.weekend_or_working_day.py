def weekend_or_working_day(day: str):
    working_days = {'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'}
    weekend = {'Saturday', 'Sunday'}

    if day in working_days:
        return 'Working day'

    elif day in weekend:
        return 'Weekend'

    else:
        return 'Error'


day = input()
print(weekend_or_working_day(day))
