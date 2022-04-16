favorite_book = input()
books_checked = -1

while True:
    book = input()
    books_checked += 1
    if book == favorite_book:
        print(f"You checked {books_checked} books and found it.")
        break
    if book == 'No More Books':
        print("The book you search is not here!")
        print(f"You checked {books_checked} books.")
        break