def day_of_week(num: int):
    day_of_week = {
        1: 'Monday',
        2: 'Tuesday',
        3: 'Wednesday',
        4: 'Thursday',
        5: 'Friday',
        6: 'Saturday',
        7: 'Sunday'
    }

    if num in day_of_week:
        return day_of_week[num]

    else:
        return 'Error'


number = int(input())
print(day_of_week(number))
