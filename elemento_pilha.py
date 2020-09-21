class ElementoPilha:

    def __init__(self, valor):
        self.__valor = valor
        self.__anterior = None

    @property
    def valor(self):
        return self.__valor

    @property
    def anterior(self):
        return self.__anterior

    @valor.setter
    def valor(self):
        self.__valor = valor

    @anterior.setter
    def anterior(self, anterior):
        self.__anterior = anterior
