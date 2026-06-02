with open('Data/books.txt') as books:
    list_books = books.readlines()

with open('Output/library_report.txt', mode = 'w') as write_report:
    write_report.write('Library Report\n'
                       '===============\n'
                       f'Total books: {len(list_books)}'
                       '\n'
                       '\nBooks: \n')

    counter = 1
    for book in list_books:
        clear_book_name = book.strip()
        write_report.write(f'{counter}. {clear_book_name}\n')
        counter += 1

        with open(f'Output/{clear_book_name}.txt', mode='w') as completed_files:
            completed_files.write(f'Book: {clear_book_name}\nStatus: Available')