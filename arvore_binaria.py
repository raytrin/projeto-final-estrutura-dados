class No:
    def __init__(self, lista):
        self.lista = lista
        self.esquerda = None
        self.direita = None

class ArvoreBinariaBusca:
    def __init__(self):
         self.raiz = None

    def insere(self, lista):
        novo = No(lista)

        if self.raiz is None:
            self.raiz = novo
            return
        
        
        atual = self.raiz
            
        while True:
            pai = atual
            if lista.nome < atual.lista.nome:
                atual = atual.esquerda  
                if atual is None:       
                    pai.esquerda = novo 
                    return

            else:
                atual = atual.direita
                if atual == None:
                    pai.direita = novo
                    return
                        
    def pesquisa(self, nome):
        atual = self.raiz

        while atual is not None:
        
            if nome == atual.lista.nome:
                return atual.lista
            
            elif nome < atual.lista.nome:
                atual = atual.esquerda

            else:
                atual = atual.direita

        return None

    def remover(self, nome):
        if self.raiz is None: 
            return False

        atual = self.raiz
        pai = None
        esta_na_esquerda = False
 
        while atual is not None and atual.lista.nome != nome:
            pai = atual
            if nome < atual.lista.nome:
                esta_na_esquerda = True
                atual = atual.esquerda
            else:
                esta_na_esquerda = False
                atual = atual.direita
 
        if atual is None:
            return False  
 
        
        if atual.esquerda is None and atual.direita is None:
            if atual is self.raiz:
                self.raiz = None
            elif esta_na_esquerda:
                pai.esquerda = None
            else:
                pai.direita = None
 
        
        elif atual.esquerda is None or atual.direita is None:

            filho = atual.direita if atual.esquerda is None else atual.esquerda

            if atual is self.raiz:
                self.raiz = filho

            elif esta_na_esquerda:
                pai.esquerda = filho

            else:
                pai.direita = filho
 
        else:
            sucessor_pai = atual
            sucessor = atual.direita

            while sucessor.esquerda is not None:
                sucessor_pai = sucessor
                sucessor = sucessor.esquerda
 
            atual.lista = sucessor.lista 
 
            if sucessor_pai.esquerda is sucessor:
                sucessor_pai.esquerda = sucessor.direita

            else:
                sucessor_pai.direita = sucessor.direita
 
        return True
 
    def exibe(self):
        self._exibe_recursivo(self.raiz)
 
    def _exibe_recursivo(self, no):
        if no is not None:
            self._exibe_recursivo(no.esquerda)
            d = no.lista
            print(f"Nome: {d.nome} | Idade: {d.idade} | Telefone: {d.telefone} | Cidade: {d.cidade}")
            self._exibe_recursivo(no.direita)

    def minimo(self):
    
        if self.raiz is None:
            return None

        atual = self.raiz
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual.lista

    def maximo(self):
        
        if self.raiz is None:
            return None

        atual = self.raiz
        while atual.direita is not None:
            atual = atual.direita
        return atual.lista

    def lista_em_ordem(self):
        
        resultado = []
        self._coleta_em_ordem(self.raiz, resultado)
        return resultado

    def _coleta_em_ordem(self, no, resultado):
        if no is not None:
            self._coleta_em_ordem(no.esquerda, resultado)
            resultado.append(no.lista)
            self._coleta_em_ordem(no.direita, resultado)