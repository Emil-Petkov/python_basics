def vacation_books_list(n_pages: int, pages_per_hour: int, days: int):
    needed_time = int((n_pages / pages_per_hour) / days)

    return needed_time


n_pages = int(input())
pages_per_hour = int(input())
days = int(input())

print(vacation_books_list(n_pages, pages_per_hour, days))
