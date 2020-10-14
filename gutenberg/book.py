import requests
from typing import List, Union
from author import Author


class Book:

    def __init__(
            self,
            id,
            title,
            authors: List[Author],
            subjects: List[str],
            languages: List[str],
            copyright: Union[bool, None],
            formats: dict,
            download_count):
        self.id = str(id)
        self.title = title
        self.authors = authors
        self.subjects = subjects
        self.languages = languages
        self.copyright = copyright
        self.formats = formats
        self.download_count = download_count

    def to_string(self):
        return f'''Livro -> 
        id: {self.id}
        título: {self.title} 
        autores: {' - '.join([x.name for x in self.authors])}
        domínio publico: {"sim" if not self.copyright else "não"}
        download em epub: {"sim" if self.epub_is_avaliable() else "não"}'''

    def epub_is_avaliable(self) -> bool:
        epub_formats = ['application/epub+zip']
        formats = self.formats.keys()

        for i in epub_formats:
            if i in formats:
                return True

        return False

    def epub_download(self, file_path: str):
        if not self.epub_is_avaliable():
            print(
                f'O livro ({self.title}) não está disponível para download no formato epub')
            return

        print('Fazendo o download do livro ' + self.title + '...........')
        response = requests.get(self.formats['application/epub+zip'])

        if response.status_code == requests.codes.OK:
            with open(file_path, 'wb') as file:
                file.write(response.content)

            print('Download finalizado. O arquivo está disponível em: ' + file_path)
        else:
            print('Erro ao fazer o download')
