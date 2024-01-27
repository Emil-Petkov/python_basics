
the_book = input()
search = input()
count_books = 0

while not search == 'No More Books':
    if not search == the_book:
        count_books += 1

    else:
        print(f'You checked {count_books} books and found it.')
        break

    search = input()


else:
    print(f'The book you search is not here!\nYou checked {count_books} books.')
