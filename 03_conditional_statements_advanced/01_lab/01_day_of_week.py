def day_of_week(day: int):
    week_map = {
        1: 'Monday',
        2: 'Tuesday',
        3: 'Wednesday',
        4: 'Thursday',
        5: 'Friday',
        6: 'Saturday',
        7: 'Sunday'
    }

    if day in week_map:
        return week_map[day]

    return 'Error'


day = int(input())
print(day_of_week(day))
