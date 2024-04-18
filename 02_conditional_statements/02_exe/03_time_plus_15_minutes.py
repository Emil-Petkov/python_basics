def time_plus_15_minutes(h: int, m: int):
    time_in_minutes = (h * 60) + (m + 15)  # plus fifteen minutes

    current_hour = time_in_minutes // 60
    current_minutes = time_in_minutes % 60

    if current_hour > 23:
        current_hour = 0

    elif current_minutes > 59:
        current_hour += 1

    if current_minutes < 10:
        return f'{current_hour}:{current_minutes:02d}'

    else:
        return f'{current_hour}:{current_minutes}'


hours = int(input())
minutes = int(input())
print(time_plus_15_minutes(hours, minutes))
