from Nodo import *
from NodoAleatorio import *
import  numpy as np
from Pokemon import *

class Arbol:
    def __init__(self,pokemonUser,pokemonMachine,multiplicadora):
        self.NodoMax = Nodo(0,1)
        TotalValores = np.array([])

        #daño que la maquina hace al usuario
        TotalValores = np.append(TotalValores,
                        pokemonMachine.Ataques[0].Potencia*(pokemonMachine.Ataques[0].Precision/100)*
                                 multiplicadora[pokemonMachine.Ataques[0].Tipo][pokemonUser.Tipos[0]])

        TotalValores = np.append(TotalValores,
                                 pokemonMachine.Ataques[1].Potencia * (pokemonMachine.Ataques[1].Precision / 100) *
                                 multiplicadora[pokemonMachine.Ataques[1].Tipo][pokemonUser.Tipos[0]])

        TotalValores = np.append(TotalValores,
                                 pokemonMachine.Ataques[2].Potencia * (pokemonMachine.Ataques[2].Precision / 100) *
                                 multiplicadora[pokemonMachine.Ataques[2].Tipo][pokemonUser.Tipos[0]])
        TotalValores = np.append(TotalValores,
                                 pokemonMachine.Ataques[3].Potencia * (pokemonMachine.Ataques[3].Precision / 100) *
                                 multiplicadora[pokemonMachine.Ataques[3].Tipo][pokemonUser.Tipos[0]])


        self.NodoAleatorioMax = NodoAleatorio(TotalValores,1)
        self.NodosMin = [Nodo(TotalValores[0],-1),Nodo(TotalValores[1],-1),Nodo(TotalValores[2],-1),Nodo(TotalValores[3],-1)]
        TotalValoresMin = np.array([])

        # daño que el usuario nos hace
        TotalValoresMin = np.append(TotalValores,
                                 pokemonUser.Ataques[0].Potencia * (pokemonUser.Ataques[0].Precision / 100) *
                                 multiplicadora[pokemonUser.Ataques[0].Tipo][pokemonMachine.Tipos[0]])
        TotalValoresMin = np.append(TotalValores,
                                    pokemonUser.Ataques[1].Potencia * (pokemonUser.Ataques[1].Precision / 100) *
                                    multiplicadora[pokemonUser.Ataques[1].Tipo][pokemonMachine.Tipos[0]])
        TotalValoresMin = np.append(TotalValores,
                                    pokemonUser.Ataques[2].Potencia * (pokemonUser.Ataques[2].Precision / 100) *
                                    multiplicadora[pokemonUser.Ataques[2].Tipo][pokemonMachine.Tipos[0]])
        TotalValoresMin = np.append(TotalValores,
                                    pokemonUser.Ataques[3].Potencia * (pokemonUser.Ataques[3].Precision / 100) *
                                    multiplicadora[pokemonUser.Ataques[3].Tipo][pokemonMachine.Tipos[0]])


        #Heuristica: Dano que le hacemos al usuario menos el dano que el usuario nos hace
        self.NodosAleatoriosMin =[NodoAleatorio(TotalValores[0]-TotalValoresMin,-1),
                                  NodoAleatorio(TotalValores[1]-TotalValoresMin,-1),
                                  NodoAleatorio(TotalValores[2]-TotalValoresMin,-1),
                                  NodoAleatorio(TotalValores[3]-TotalValoresMin,-1)]


        self.NodosAleatoriosMin[0].setValor(self.NodosAleatoriosMin[0].Heuristicas[0]*0.25+
                                            self.NodosAleatoriosMin[0].Heuristicas[1] * 0.25+
                                            self.NodosAleatoriosMin[0].Heuristicas[2]*0.25+
                                            self.NodosAleatoriosMin[0].Heuristicas[3]*0.25)

        self.NodosAleatoriosMin[1].setValor(self.NodosAleatoriosMin[1].Heuristicas[0] * 0.25 +
                                            self.NodosAleatoriosMin[1].Heuristicas[1] * 0.25 +
                                            self.NodosAleatoriosMin[1].Heuristicas[2] * 0.25 +
                                            self.NodosAleatoriosMin[1].Heuristicas[3] * 0.25)

        self.NodosAleatoriosMin[2].setValor(self.NodosAleatoriosMin[2].Heuristicas[0] * 0.25 +
                                            self.NodosAleatoriosMin[2].Heuristicas[1] * 0.25 +
                                            self.NodosAleatoriosMin[2].Heuristicas[2] * 0.25 +
                                            self.NodosAleatoriosMin[2].Heuristicas[3] * 0.25)

        self.NodosAleatoriosMin[3].setValor(self.NodosAleatoriosMin[3].Heuristicas[0] * 0.25 +
                                            self.NodosAleatoriosMin[3].Heuristicas[1] * 0.25 +
                                            self.NodosAleatoriosMin[3].Heuristicas[2] * 0.25 +
                                            self.NodosAleatoriosMin[3].Heuristicas[3] * 0.25)

        self.NodoAleatorioMax.setValor(self.NodosAleatoriosMin[0].Valor*0.25+
                                       self.NodosAleatoriosMin[1].Valor*0.25+
                                       self.NodosAleatoriosMin[2].Valor*0.25+
                                       self.NodosAleatoriosMin[3].Valor*0.25)

        for i in self.NodosAleatoriosMin:
            print(i.Valor)

        for i in pokemonMachine.Ataques:
            print(i.Nombre)

    #Obtiene la heuristica mas alta y toma la decision
    def getDecision(self):
        mayor = 0
        for i in range(0,4):
            if self.NodosAleatoriosMin[i].Valor > self.NodosAleatoriosMin[mayor].Valor:
                mayor = i
        print(mayor)
        return  mayor




