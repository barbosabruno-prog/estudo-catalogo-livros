# CATÁLOGO PARA LIVROS

class Livro:
    
    def __init__(self, titulo, editora, autor, isbn):
        self.titulo = titulo
        self.editora = editora
        self.autor = autor
        self.isbn = isbn

    def imprime_livro(self):
        print(f'Título: {self.titulo} \n Editora: {self.editora} \n Autor: {self.autor} \n ISBN: {self.isbn} \n')

class Catalogo:

    def __init__(self, catalogo_livros = []):
        self.catalago_livros = catalogo_livros
    
    def busca_livro(self):
        modo_input = int(input('Digite o modo que você quer buscar um livro: \n'
            '1 - Por Título \n'
            '2 - Por Editora \n'
            '3 - Por Autor \n'
            '4 - Por ISBN \n'
            '>>> '
        ))

        match modo_input:
            case 1:
                procurar = input('Digite o título que deseja procurar: ').lower()
                
                controle = 0

                for i in self.catalago_livros:
                    if procurar == i.titulo.lower():
                        i.imprime_livro()
                        controle += 1

            case 2:
                procurar = input('Digite a Editora que deseja procurar: ').lower()
                
                controle = 0

                for i in self.catalago_livros:
                    if procurar == i.editora.lower():
                        i.imprime_livro()
                        controle += 1

            case 3:
                procurar = input('Digite o autor que deseja procurar: ').lower()
                
                controle = 0

                for i in self.catalago_livros:
                    if procurar == i.autor.lower():
                        i.imprime_livro()
                        controle += 1
                
            case 4:
                procurar = input('Digite o ISBN que deseja procurar: ').lower()
                
                for i in self.catalago_livros:
                    if procurar == i.isbn.lower():
                        i.imprime_livro()
                        controle += 1
            
        if controle == 0:
            print('Resultado não encontrado!')

    def insereLivro(self):
        escolha = input('Deseja cadastrar um livro? (S/N)').upper()

        if escolha == "S":
            while escolha == "S":
                # titulo = input('Digite o Título do Livro: ')
                # editora = input('Digite a Editora do Livro: ')
                # autor = input('Digite o Autor do Livro: ')
                # isbn = input('Digite o ISBN do Livro: ')
                
                # livro_para_inserir = Livro(titulo, editora, autor, isbn)
            
                # self.catalago_livros.append(livro_para_inserir)

                # escolha = input('Deseja cadastrar mais algum livro? (S/N)').upper()

                # ***versão para testar:***
                livro1 = Livro('A Rainha dos Condenados', 'Rocco', 'Anne Rice', '6555321377')
                livro2 = Livro('Box Trilogia O Senhor dos Anéis', 'HarperColins', 'J R R Tolkien', '8595086354')
                livro3 = Livro('Box Harry Poter', 'Rocco', 'J K Rowling', '6555320478')
                livro4 = Livro('Cthulhu Mythos Tales', 'Canterbury Classics', 'H P Lovecraft', '1684121337')
                self.catalago_livros.append(livro1)
                self.catalago_livros.append(livro2)
                self.catalago_livros.append(livro3)
                self.catalago_livros.append(livro4)
                print('Livros para teste cadastrados com sucesso!')
                break

        elif escolha == "N":
            print('Nenhum livro cadastrado!')
        else:
            print('Escolha inválida!')
            self.insereLivro()
            

catalogo = Catalogo()

catalogo.insereLivro()

for i in catalogo.catalago_livros:
    i.imprime_livro()

catalogo.busca_livro()
