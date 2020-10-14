import gutendex

# gutendex ------------------------------------
books = []

# busca os livros pelos IDs

# books = gutendex.get_books_by_ids(55682, 54829)
# for book in books:
#     print(book.to_string())

# busca os livros por pesquisa

# text = input('texto da pesquisa: ')
# books = gutendex.search_books(text)
# for book in books:
#     print(book.to_string())

# fazer o download dos livros
if books:
    download_books = input('baixar os livros? (s/n) ')
    if download_books.lower() == 's':
        for book in books:
            book.epub_download(
                'downloads/' + book.title.lower().replace(' ', '-') + '.epub')
