import math


def lunch_break(series: str, duration_episode: int, l_break: int):
    lunch_time = l_break / 8
    time_to_relax = l_break / 4

    free_time = l_break - lunch_time - time_to_relax

    diff = math.ceil(abs(duration_episode - free_time))
    if free_time >= duration_episode:
        return f'You have enough time to watch {series} and left with {diff} minutes free time.'

    return f"You don't have enough time to watch {series}, you need {diff} more minutes."


series = input()
duration_of_episode = int(input())
duration_of_lunch_break = int(input())

print(lunch_break(series, duration_of_episode, duration_of_lunch_break))
