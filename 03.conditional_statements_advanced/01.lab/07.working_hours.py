def working_hours(hour: int, day: str):
    work_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

    if 10 <= hour <= 18 and day in work_days:
        return 'open'

    return 'closed'


hour = int(input())
day_of_week = input()
print(working_hours(hour, day_of_week))
