def sum_seconds(f_time: int, s_time: int, t_time: int):
    sum_time = f_time + s_time + t_time

    minutes = sum_time // 60
    seconds = sum_time % 60

    return f'{minutes}:{seconds:02d}'


first_time = int(input())
second_time = int(input())
third_time = int(input())

print(sum_seconds(first_time, second_time, third_time))
