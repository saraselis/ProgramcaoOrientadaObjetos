class EmptyLinkedList(Exception):
    def __init__(self):
        super().__init__('Lista vazia')


class Aluno:
    def __init__(self, nome: str, nota: float):
        self.__nome = nome
        self.__nota = nota
        self.__prox = None

    def __repr__(self):
        return f'{self.__nome}:{self.__nota}'

    def __lt__(self, outro_aluno):
        return self.__nota < outro_aluno.__nota

    def __gt__(self, outro_aluno):
        return self.__nota > outro_aluno.__nota

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

        if atual == None:
            raise EmptyLinkedList

        if atual.prox == None:
            self.__final = None
            self.__inicio = None
            return atual

        while atual.prox != self.__final:
            atual = atual.prox
        atual.prox = None
        retorno = self.__final
        self.__final = atual
        return retorno

    def size(self):
        if self.__inicio == None:
            return 0
        atual = self.__inicio
        tamanho = 1
        while atual != self.__final:
            atual = atual.prox
            tamanho += 1
        return tamanho

    def sort(self):
        for _ in range(self.size()):
            atual = self.__inicio
            anterior = self.__inicio
            while atual != self.__final:
                if atual > atual.prox:
                    novo_atual = atual.prox
                    atual.prox = novo_atual.prox
                    novo_atual.prox = atual
                    if atual == self.__inicio:
                        self.__inicio = novo_atual
                    else:
                        anterior.prox = novo_atual

                if atual.prox == None:
                    self.__final = atual
                else:
                    anterior = atual
                    atual = atual.prox

    def __repr__(self):
        saida = ''
        atual = self.__inicio
        while atual != None: 
            saida += f'{atual}'
            atual = atual.prox
            if atual != None:
                saida += ' -> '
        return f'[{saida}]'


lista_nao_ligada = [Aluno('Sara', 9.8), Aluno('Lucas', 7.8), Aluno('Sabrina', 8.8)]
print(lista_nao_ligada)
lista_nao_ligada.sort()
print(lista_nao_ligada)


lista = ListaLigada()
lista.append(Aluno('Sara', 9.8))
lista.append(Aluno('Lucas', 7.8))
lista.append(Aluno('Victoria', 9.8) )
lista.append(Aluno('Sabrina', 8.8) )
print(lista, lista.size())
lista.sort()
print(lista)
# print(lista.pop())
# print(lista.pop())
# print(lista)



    
