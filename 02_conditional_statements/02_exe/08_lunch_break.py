import math


def lunch_break(series_name: str, episode_duration: int, res_duration: int):
    lunch_time = res_duration / 8
    relax_time = res_duration / 4

    time_per_series = res_duration - (lunch_time + relax_time)

    diff = abs(episode_duration - time_per_series)

    if time_per_series >= episode_duration:
        return f'You have enough time to watch {series_name} and left with {math.ceil(diff)} minutes free time.'

    else:
        return f'You don\'t have enough time to watch {series_name}, you need {math.ceil(diff)} more minutes.'


series_name = input()
episode_duration = int(input())
res_duration = int(input())
print(lunch_break(series_name, episode_duration, res_duration))
