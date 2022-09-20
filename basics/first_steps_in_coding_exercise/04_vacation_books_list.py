count_pages_per_book = int(input())
read_pages_per_hour = int(input())
count_days = int(input())

total = (count_pages_per_book // read_pages_per_hour) // count_days

print(total)