'''CATÁLOGO PARA LIVROS'''

class Livro:
    def __init__(self, titulo, editora, autor, isbn):
        self.titulo = titulo
        self.editora = editora
        self.autor = autor
        self.isbn = isbn

    def setTitulo (self, titulo):
        self.titulo = titulo

    def setEditora (self, editora):
        self.editora = editora

    def setAutor (self, autor):
        self.editora = autor

    def setISBN (self, isbn):
        self.isbn = isbn

#def getLivro():
    # #implementar busca de livro

def imprimeLivro(livroConsultado):
    print('Título: {} \n'
        'Editora: {} \n'
        'Autor: {} \n'
        'ISBN: {}')

livros = []

def insereLivro():
    a = input('Digite o Título do Livro: ')
    b = input('Digite a Editora do Livro: ')
    c = input('Digite o Autor do Livro: ')
    d = input('Digite o ISBN do Livro: ')
    liv_inserir = Livro(a, b, c, d)



livro1 = Livro('A Rainha dos Condenados', 'Rocco', 'Anne Rice', '85-32-0031-5')

