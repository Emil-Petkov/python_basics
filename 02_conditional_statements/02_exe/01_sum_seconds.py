def sum_seconds(f_time: int, s_time: int, t_time: int):
    sum_seconds = f_time + s_time + t_time

    minutes = sum_seconds // 60
    seconds = sum_seconds % 60

    if seconds < 10:
        return f'{minutes}:{seconds:02d}'

    else:
        return f'{minutes}:{seconds}'


first_time_in_seconds = int(input())
second_time_in_seconds = int(input())
third_time_in_seconds = int(input())
print(sum_seconds(first_time_in_seconds, second_time_in_seconds, third_time_in_seconds))
