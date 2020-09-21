from pilha import Pilha
from fila import Fila


class TesteFilaPilha:

    def __init__(self, max_elementos):
        self.__pilha = Pilha(max_elementos)
        self.__fila = Fila(max_elementos)

    @property
    def pilha(self):
        return self.__pilha

    @property
    def fila(self):
        return self.__fila

    def testa_encher_pilha(self):
        for i in range(self.pilha.max_elementos + 1):
            try:
                self.pilha.push(i+1)
            except Exception as e:
                print(e)
                break

    def testa_esvaziar_pilha(self):
        for i in range(self.pilha.contador + 1):
            try:
                self.pilha.pop()
            except Exception as e:
                print(e)
                break

    def testa_encher_fila(self):
        for i in range(1, self.fila.max_elementos + 2):
            try:
                self.fila.insere(i)
            except Exception as e:
                print(e)
                break

    def testa_esvaziar_fila(self):
        while True:
            try:
                self.fila.remove()
            except Exception as e:
                print(e)
                break


teste = TesteFilaPilha(5)

print('--------------- Pilha ---------------\n')
print('Inserindo elementos na pilha:')
teste.testa_encher_pilha()
print('\nEsvaziando a pilha:')
teste.testa_esvaziar_pilha()

print('\n')
print('--------------- Fila ---------------\n')
print('Inserindo elementos na fila:')
teste.testa_encher_fila()

print('\nEsvaziando a fila: \n')
teste.testa_esvaziar_fila()
