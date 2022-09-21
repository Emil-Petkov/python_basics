input_book = input()

input_line = input()

count_books = 0

is_book_found = False

while input_line != 'No More Books':
    if input_line == input_book:
        is_book_found = True
        break

    count_books += 1
    input_line = input()

if is_book_found:  # if is_book_found == True
    print(f"You checked {count_books} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {count_books} books.")
