with open('Data/books.txt') as books:
    list_books = books.readlines()

with open('Output/library_report.txt', mode = 'w') as write_report:
    write_report.write('Library Report\n'
                       '===============\n'
                       f'Total books: {len(list_books)}'
                       '\n'
                       'Books')


    