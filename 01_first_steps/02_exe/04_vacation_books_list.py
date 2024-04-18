import math


def vacation_books(pages: int, pages_per_hour: int, day: int):
    total_hours = pages / pages_per_hour
    hour_per_day = total_hours / day

    return math.floor(hour_per_day)


n_pages = int(input())
read_pages_per_hour = int(input())
n_days = int(input())
print(vacation_books(n_pages, read_pages_per_hour, n_days))
