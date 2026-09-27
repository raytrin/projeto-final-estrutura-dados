from utils.atribui_cidade import atribui_cidade


class Elemento:
    def __init__(self, nome, idade, telefone):
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
        self.cidade = atribui_cidade()
        self.proximo = None

    def mostra_elemento(self):
        print(f"Nome: {self.nome} | Idade: {self.idade} | Telefone: {self.telefone} | Cidade: {self.cidade}")

class ListaEncadeada:
    def __init__(self):
        self.primeiro = None

    def lista_vazia(self):
        return self.primeiro is None

    def tamanho_lista(self):
        tamanho = 0
        atual = self.primeiro

        if self.lista_vazia():
            return 0

        while atual != None:
            tamanho += 1
            atual = atual.proximo
        return tamanho

    def inserir_inicio(self, nome, idade, telefone):
        novo = Elemento(nome, idade, telefone)

        if self.lista_vazia():
            self.primeiro = novo
            return

        novo.proximo = self.primeiro
        self.primeiro = novo

    def mostrar_lista(self):
        atual = self.primeiro

        if self.lista_vazia():
            print('Lista vazia')
            return
        
        while atual != None:
            atual.mostra_elemento()
            atual = atual.proximo


    def inserir_fim(self, nome, idade, telefone):
        novo = Elemento(nome, idade, telefone)

        if self.lista_vazia():
            self.primeiro = novo
            return novo

        atual = self.primeiro

        while atual.proximo != None:
            atual = atual.proximo

        atual.proximo = novo
        return novo
    

    def busca_por_nome(self, nome):

        atual = self.primeiro

        while atual is not None:
            if atual.nome == nome:
                return atual
            atual = atual.proximo

        return None

   