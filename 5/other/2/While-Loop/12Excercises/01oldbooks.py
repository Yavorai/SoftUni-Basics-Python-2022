wanted_book = input()

current_book = input()
books_count = 0
has_found_it = False

while current_book != 'No More Books':
    books_count += 1
    if current_book == wanted_book:
        has_found_it = True
        break
    current_book = input()

if has_found_it:
    print(f'You checked {books_count - 1} books and found it.')
else:
    print(f'The book you search is not here!')
    print(f'You checked {books_count} books.')
