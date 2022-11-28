book_name = input()

count_books = 0
is_book_found = False

line = input()

while line != "No More Books":
     current_book = line

     if current_book == book_name:
         print(f'You checked {count_books} books and found it.')
         is_book_found = True
         break

     count_books += 1
     line = input()

if not is_book_found:
    print('The book you search is not here!')
    print(f'You checked {count_books} books.')
