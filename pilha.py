from elemento_pilha import ElementoPilha


class Pilha:

    def __init__(self):
        self.__topo = None
        self.__contador = 0

    @property
    def contador(self):
        return self.__contador

    @contador.setter
    def contador(self, contador):
        self.__contador = contador

    def push(self, valor, max_elementos):
        if(self.contador < max_elementos):
            tmp = ElementoPilha(valor)
            tmp.anterior = self.__topo
            self.__topo = tmp
            self.contador += 1
        else:
            raise Exception('Tamanho máximo excedido!')

    def pop(self):
        self.contador -= 1
        if(self.__topo.anterior):
            self.__topo = self.__topo.anterior
        else:
            raise Exception('Pilha vazia!')
    
    def elemento_topo(self):
        topo = self.__topo
        return (topo, topo.anterior)
