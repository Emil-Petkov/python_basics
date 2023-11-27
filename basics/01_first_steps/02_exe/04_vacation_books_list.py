num_pages = int(input())
num_pages_per_one_hour = int(input())
days = int(input())

need_hours_per_day = (num_pages / num_pages_per_one_hour) / days

print(round(need_hours_per_day))
