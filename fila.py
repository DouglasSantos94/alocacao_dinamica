from elemento_fila import ElementoFila


class Fila:

    def __init__(self, max_elementos):
        self.__topo = None
        self.__inicio = None
        self.__max_elementos = max_elementos
        self.__contador = 0

    @property
    def max_elementos(self):
        return self.__max_elementos

    @property
    def contador(self):
        return self.__contador

    @contador.setter
    def contador(self, contador):
        self.__contador = contador

    def insere(self, valor):
        self.contador += 1
        if(self.contador <= self.max_elementos):
            tmp = ElementoFila(valor)
            if not self.__inicio:
                self.__inicio = tmp
                self.__topo = tmp
            elif not self.__inicio.proximo:
                self.__inicio.proximo = tmp
                self.__topo = self.__inicio.proximo
            else:
                self.__topo.proximo = tmp
                self.__topo = self.__topo.proximo
            self.imprime_topo()
        else:
            raise Exception('Fila lotada!')

    def remove(self):
        self.contador -= 1
        if self.__inicio:
            self.imprime_removido()
            self.__inicio = self.__inicio.proximo
        else:
            self.__topo = None
            raise Exception('Fila vazia!')
    
    def imprime_topo(self):
        print('Valor topo: ', self.__topo.valor)

    def imprime_removido(self):
        print('Removido: ', self.__inicio.valor)
