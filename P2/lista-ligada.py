class Aluno:
    def __init__(self, nome: str, nota: float):
        self.__nome = nome
        self.__nota = nota
        self.__prox = None

    def __repr__(self):
        return f'{self.__nome}:{self.__nota}'

    @property
    def prox(self):
        return self.__prox
    
    @prox.setter
    def prox(self, prox):
        self.__prox = prox


class ListaLigada:
    def __init__(self):
        self.__inicio = None
        self.__final = None

    def append(self, aluno: Aluno):
        if self.__inicio == None:
            self.__inicio = aluno
            self.__final = aluno
        else:
            self.__final.prox = aluno
            self.__final = aluno

    def pop(self):
        atual = self.__inicio
        while atual.prox != self.__final:
            atual = atual.prox
        atual.prox = None
        self.__final = atual
        return atual

    def sort(self):
        pass

    def __repr__(self):
        saida = ''
        atual = self.__inicio
        while atual != None: 
            saida = saida + f'{atual} '
            atual = atual.prox
        return saida

sara = Aluno('Sara', 9.8)
sabrina = Aluno('Sabrina', 9.8) 
lista = ListaLigada()
lista.append(sara)
lista.append(sabrina)
print(lista)
print(lista.pop())
print(lista)



    
