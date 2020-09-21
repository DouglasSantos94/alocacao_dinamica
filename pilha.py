from elemento_pilha import ElementoPilha


class Pilha:

    def __init__(self, max_elementos):
        self.__topo = None
        self.__contador = 0
        self.__max_elementos = max_elementos

    @property
    def contador(self):
        return self.__contador

    @property
    def max_elementos(self):
        return self.__max_elementos

    @contador.setter
    def contador(self, contador):
        self.__contador = contador

    def push(self, valor):
        if(self.contador < self.max_elementos):
            tmp = ElementoPilha(valor)
            tmp.anterior = self.__topo
            self.__topo = tmp
            self.contador += 1
            self.imprime_valor_anterior()
        else:
            raise Exception('Tamanho máximo excedido!')

    def pop(self):
        self.contador -= 1
        if(self.__topo):
            print('Removido: ', self.__topo.valor)
            self.__topo = self.__topo.anterior
        else:
            raise Exception('Pilha vazia!')
    
    def imprime_valor_anterior(self):
        print('Valor: ', self.__topo.valor)
        texto = 'Anterior: {}'.format(
            self.__topo.anterior.valor if self.__topo.anterior else self.__topo.anterior)
        print(texto)
