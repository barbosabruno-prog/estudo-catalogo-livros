#CATÁLOGO PARA LIVROS

class Livro:
    def __init__(self, titulo, editora, autor, isbn):
        self.titulo = titulo
        self.editora = editora
        self.autor = autor
        self.isbn = isbn

    def imprimeLivro(self):
        print(f'Título: {self.titulo} \n Editora: {self.editora} \n Autor: {self.autor} \n ISBN: {self.isbn} \n')

class Catalogo:

    def __init__(self, livro):
        self.livro = livro
    
    def getLivro():
            #implementar busca de livro
            pass

    def insereLivro():
        titulo = input('Digite o Título do Livro: ')
        editora = input('Digite a Editora do Livro: ')
        autor = input('Digite o Autor do Livro: ')
        isbn = input('Digite o ISBN do Livro: ')
        
        livro_para_inserir = Livro(titulo, editora, autor, isbn)
        
        return livro_para_inserir


livro1 = Livro('A Rainha dos Condenados', 'Rocco', 'Anne Rice', '6555321377')
livro2 = Livro('Box Trilogia O Senhor dos Anéis ', 'HarperColins', 'J R R Tolkien', '8595086354')
livro3 = Livro('Box Harry Poter', 'Rocco', 'J K Rowling', '6555320478')
livro4 = Livro('Cthulhu Mythos Tales', 'Canterbury Classics', 'H P Lovecraft', '1684121337')

livros = {
    '6555321377' : livro1,
    '8595086354' : livro2,
    '6555320478' : livro3,
    '1684121337' : livro4
}
for i in livros:
    livros[i].imprimeLivro()
