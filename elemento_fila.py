class ElementoFila:

    def __init__(self, valor):
        self.__valor = valor
        self.__proximo = None

    @property
    def valor(self):
        return self.__valor

    @property
    def inicio(self):
        return self.__inicio

    @property
    def proximo(self):
        return self.__proximo

    @valor.setter
    def valor(self):
        self.__valor = valor

    @proximo.setter
    def proximo(self, proximo):
        self.__proximo = proximo
