import math

name_of_movie = input()
duration_episode = int(input())
lunch_break = int(input())

lunch_time = lunch_break / 8
rest_time = lunch_break / 4

total_time_without_the_movie = lunch_break - lunch_time - rest_time

if total_time_without_the_movie >= duration_episode:
    print(
        f'You have enough time to watch {name_of_movie} and left with {math.ceil(total_time_without_the_movie - duration_episode)} minutes free time.')
else:
    print(
        f"You don't have enough time to watch {name_of_movie}, you need {math.ceil(duration_episode - total_time_without_the_movie)} more minutes.")
