from elemento_pilha import ElementoPilha


class Pilha:

    def __init__(self, max_elementos):
        self.__topo = None
        self.__contador = 0
        self.__max_elementos = max_elementos

    @property
    def topo(self):
        return self.__topo

    @property
    def contador(self):
        return self.__contador

    @property
    def max_elementos(self):
        return self.__max_elementos

    @topo.setter
    def topo(self, topo):
        self.__topo = topo

    @contador.setter
    def contador(self, contador):
        self.__contador = contador

    def push(self, valor):
        if(self.contador < self.max_elementos):
            tmp = ElementoPilha(valor)
            tmp.anterior = self.topo
            self.topo = tmp
            self.contador += 1
        else:
            raise Exception('Tamanho máximo excedido!')

    def pop(self):
        self.contador -= 1
        if(self.topo.anterior):
            self.topo = self.topo.anterior
            return self.topo.valor
        else:
            raise Exception('Pilha vazia!')
