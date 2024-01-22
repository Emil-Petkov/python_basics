def time_plus_fifteen_minutes(hour: int, minutes: int):
    total_time_in_minutes = (hour * 60) + minutes + 15

    hours = total_time_in_minutes // 60
    minutes = total_time_in_minutes % 60

    if hours > 23:
        hours = 0

    if minutes > 59:
        hours += 1
        minutes = 0

    return hours, minutes


hours = int(input())
minutes = int(input())
h, m = time_plus_fifteen_minutes(hours, minutes)

print(f'{h}:{m:02d}')
