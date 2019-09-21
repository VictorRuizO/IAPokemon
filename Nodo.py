from NodoAleatorio import *

class Nodo:
    def __init__(self,valor,tipo):
        self.Valor = valor
        self.Tipo = tipo
        self.Hijo = NodoAleatorio(valor,tipo)



