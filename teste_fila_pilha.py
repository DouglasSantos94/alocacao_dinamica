from pilha import Pilha
from fila import Fila


class TesteFilaPilha:

    def __init__(self, max_elementos):
        self.__pilha = Pilha()
        self.__fila = Fila()
        self.__max_elementos = max_elementos

    @property
    def pilha(self):
        return self.__pilha

    @property
    def fila(self):
        return self.__fila
    
    @property
    def max_elementos(self):
        return self.__max_elementos

    def testa_encher_pilha(self):
        for i in range(self.max_elementos + 1):
            try:
                self.pilha.push(i+1, self.max_elementos)
                topo = self.pilha.elemento_topo()[0]
                anterior = self.pilha.elemento_topo()[1]
                print('Topo: {}\nAnterior: {}'.format(topo.valor, anterior.valor if anterior else anterior))
            except Exception as e:
                print(e)
                break

    def testa_esvaziar_pilha(self):
        while True:
            try:
                print('Removido: {}'.format(self.pilha.elemento_topo()[0].valor))
                self.pilha.pop()
                print('Topo: {}'.format(self.pilha.elemento_topo()[0].valor))
            except Exception as e:
                print(e)
                break

    def testa_encher_fila(self):
        for i in range(1, self.max_elementos + 2):
            try:
                self.fila.insere(i, self.max_elementos)
                print('Valor topo: ', self.fila.elemento_topo())
            except Exception as e:
                print(e)
                break

    def testa_esvaziar_fila(self):
        while True:
            try:
                print('Inicio: ', self.fila.elemento_inicio())
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
