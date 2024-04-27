












the_book = input()
command = input()

counter_books = 0

while not command == 'No More Books':
    if command == the_book:
        print(f'You checked {counter_books} books and found it.')
        exit()

    else:
        counter_books += 1

    command = input()

print(f'The book you search is not here!\nYou checked {counter_books} books.')
