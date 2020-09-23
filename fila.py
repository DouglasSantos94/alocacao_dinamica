from elemento_fila import ElementoFila


class Fila:

    def __init__(self):
        self.__topo = None
        self.__inicio = None
        self.__contador = 0

    @property
    def contador(self):
        return self.__contador

    @contador.setter
    def contador(self, contador):
        self.__contador = contador

    def insere(self, valor, max_elementos):
        if(self.contador < max_elementos):
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
        else:
            raise Exception('Fila lotada!')
        self.contador += 1

    def remove(self):
        if self.__inicio.proximo:
            self.__inicio = self.__inicio.proximo
        else:
            self.__topo = None
            raise Exception('Fila vazia!')
        self.contador -= 1

    def elemento_topo(self):
        return self.__topo.valor

    def elemento_inicio(self):
        return self.__inicio.valor