from elemento_fila import ElementoFila


class Fila:

    def __init__(self, max_elementos):
        self.__topo = None
        self.__inicio = None
        self.__max_elementos = max_elementos
        self.__contador = 0

    @property
    def topo(self):
        return self.__topo

    @property
    def inicio(self):
        return self.__inicio

    @property
    def max_elementos(self):
        return self.__max_elementos

    @property
    def contador(self):
        return self.__contador

    @topo.setter
    def topo(self, topo):
        self.__topo = topo

    @inicio.setter
    def inicio(self, inicio):
        self.__inicio = inicio

    @contador.setter
    def contador(self, contador):
        self.__contador = contador

    def insere(self, valor):
        self.contador += 1
        if(self.contador <= self.max_elementos):
            tmp = ElementoFila(valor)
            if not self.inicio:
                self.inicio = tmp
                self.topo = tmp
            elif not self.inicio.proximo:
                self.inicio.proximo = tmp
                self.topo = self.inicio.proximo
            else:
                self.topo.proximo = tmp
                self.topo = self.topo.proximo
        else:
            raise Exception('Fila lotada!')

    def remove(self):
        self.contador -= 1
        if self.inicio:
            print('Removido: ', self.inicio.valor)
            self.inicio = self.inicio.proximo
        else:
            self.topo = None
            raise Exception('Fila vazia!')
