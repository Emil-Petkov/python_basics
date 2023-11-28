









from math import ceil

series_name = input()
duration_episode = int(input())
duration_of_rest = int(input())

lunch_time = duration_of_rest / 8
rest_time = duration_of_rest / 4

free_time = duration_of_rest - (lunch_time + rest_time)

diff = ceil(abs(duration_episode - free_time))

if free_time >= duration_episode:
    print(f'You have enough time to watch {series_name} and left with {diff} minutes free time.')

else:
    print(f"You don't have enough time to watch {series_name}, you need {diff} more minutes.")
