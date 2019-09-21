# -*- coding: utf-8 -*-
import numpy as np
from tkinter import *
from tkinter import ttk
from tkinter import font
from Ataque import *
from Pokemon import *
from Arbol import *

import threading

#Definicion de variables
multiplicador = ([[0.5, 0.5, 1,1,0.5,1,0.5,2,2,1,1,1,1,2,1,1,1,1],
                  [1,0.5,1,0.5,1,1,2,1,1,1,1,0.5,1,2,1,2,1,1],
                  [0.5,1,1,1,1,0.5,0.5,0.5,1,0.5,1,2,2,1,2,1,0.5,0.5],
                  [0.5,1,1,2,1,1,1,0,1,1,1,1,1,1,1,1,1,1],
                  [1,2,1,0.5,0.5,1,1,1,1,1,1,0.5,1,1,1,0,1,2],
                  [1,1,1,1,1,2,1,1,1,1,0,1,2,1,0.5,1,1,1],
                  [2,0.5,2,0.5,1,1,0.5,1,2,1,1,2,1,0.5,1,1,1,1],
                  [0.5,1,1,2,1,1,0.5,1,1,2,1,1,1,1,2,1,0.5,1],
                  [0.5,0.5,1,2,1,1,0.5,1,0.5,1,1,2,1,1,1,2,1,2],
                  [2,1,0.5,1,1,0,1,0.5,2,1,2,1,0.5,2,2,1,0.5,0.5],
                  [0.5,1,1,1,1,0,1,1,1,1,1,1,1,0.5,1,1,1,1],
                  [0.5,2,0.5,0.5,1,1,0.5,1,1,1,1,0,5,1,2,1,2,0.5,0.5],
                  [0.5,1,1,1,1,1,1,1,1,2,1,1,0.5,1,0,1,2,1],
                  [0,5,1,2,1,1,1,2,1,2,0.5,1,1,1,1,1,0.5,1,2],
                  [1,1,1,1,1,2,1,0.5,1,0.5,1,1,2,1,0.5,1,1,1],
                  [2,1,0.5,1,2,1,2,1,1,1,1,0.5,1,2,1,1,2,0],
                  [0,1,1,1,1,0.5,1,2,1,1,1,2,1,0.5,1,0.5,0.5,1],
                  [0.5,1,2,1,0.5,1,1,1,1,2,1,2,1,0.5,1,1,1,1]])


Ataques = np.array([Ataque("Ala de acero",0,70,90),
                    Ataque("Bomba iman",0,60,100),
                    Ataque("Cabeza de hierro",0,80,100),
                    Ataque("Cola ferrea",0,100,75),
                    Ataque("Deseo oculto",0,140,100),
                    Ataque("Disparo Espejo",0,65,85),
                    Ataque("Acua cola",1,90,90),
                    Ataque("Acua jet",1,40,100),
                    Ataque("Agua Lodosa,",1,95,85),
                    Ataque("Buceo",1,80,100),
                    Ataque("Burbuja",1,20,100),
                    Ataque("Cascada",1,80,100),
                    Ataque("Al ataque",2,90,100),
                    Ataque("Chupavidas",2,20,100),
                    Ataque("Cortefuria",2,10,95),
                    Ataque("Doble rayo",2,75,100),
                    Ataque("Doble ataque",2,25,100),
                    Ataque("Estoicismo",2,30,100),
                    Ataque("Carga dragon",3,100,75),
                    Ataque("Cola dragon",3,60,90),
                    Ataque("Ciclon",3,40,100),
                    Ataque("Cometa draco",3,140,90),
                    Ataque("Corte vacio",3,100,95),
                    Ataque("Distorsion",3,150,90),
                    Ataque("Ataque fulgor",4,130,85),
                    Ataque("Chispa",4,65,100),
                    Ataque("Chispazo",4,80,100),
                    Ataque("Colmillo rayo",4,65,95),
                    Ataque("Electrocañon",4,120,50),
                    Ataque("Electrotela",4,55,95),
                    Ataque("Bola sombra",5,80,100),
                    Ataque("Garra umbria",5,70,100),
                    Ataque("Golpe Fantasma",5,90,100),
                    Ataque("Golpe umbrio",5,120,100),
                    Ataque("Impresionar",5,30,100),
                    Ataque("Infortunio",5,50,100),
                    Ataque("Anillo igneo",6,150,90),
                    Ataque("Ascuas",6,40,100),
                    Ataque("Bomba ignea",6,100,100),
                    Ataque("Calcinacion",6,30,100),
                    Ataque("Colmillo igneo ",6,65,95),
                    Ataque("Danza llama",6,80,100),
                    Ataque("Beso drenaje",7,50,100),
                    Ataque("Brillo magico",7,80,100),
                    Ataque("Carantoña",7,90,90),
                    Ataque("Fuerza lunar",7,95,100),
                    Ataque("Luz aniquiladora",7,140,90),
                    Ataque("Viento feerico",7,40,100),
                    Ataque("Alud",8,60,100),
                    Ataque("Bola hielo",8,30,90),
                    Ataque("Canto helado",8,40,100),
                    Ataque("Carambano",8,10,100),
                    Ataque("chuzos",8,85,90),
                    Ataque("Colmillo hielo",8,65,95),
                    Ataque("A bocajarro",9,120,100),
                    Ataque("Demolicion",9,75,100),
                    Ataque("Desquite",9,60,100),
                    Ataque("Doble patada",9,30,100),
                    Ataque("Empujon",9,15,100),
                    Ataque("Espabila",9,60,100),
                    Ataque("Agarre",10,55,100),
                    Ataque("Alboroto",10,50,100),
                    Ataque("Amago",10,50,100),
                    Ataque("Antojo",10,40,100),
                    Ataque("Arañazo",10,40,100),
                    Ataque("Ariete",10,120,100),
                    Ataque("Absorber",11,20,100),
                    Ataque("Astadrenaje",11,75,100),
                    Ataque("Bomba germen",11,80,100),
                    Ataque("Brazo pincho",11,60,100),
                    Ataque("Ciclon de hojas",11,65,90),
                    Ataque("Danza petalo",11,90,100),
                    Ataque("Arrumaco",12,60,100),
                    Ataque("Bola neblina",12,70,100),
                    Ataque("Cabezazo zen",12,80,90),
                    Ataque("Coma sueños",12,100,100),
                    Ataque("Confusion",12,50,100),
                    Ataque("Onda mental",12,100,100),
                    Ataque("Antiaereo",13,50,100),
                    Ataque("Avalancha",13,75,90),
                    Ataque("Desenrollar",13,30,90),
                    Ataque("Joya de luz",13,80,100),
                    Ataque("Lanzarrocas",13,50,90),
                    Ataque("Pedrada",13,25,80),
                    Ataque("Alarido",14,55,95),
                    Ataque("Buena baza",14,50,100),
                    Ataque("Desarme",14,20,100),
                    Ataque("Golpe  bajo",14,80,100),
                    Ataque("Juego sucio",14,95,100),
                    Ataque("Ladron",14,40,100),
                    Ataque("Ataque oseo",15,25,80),
                    Ataque("Bofeton lodo",15,20,100),
                    Ataque("Bomca fango",15,65,85),
                    Ataque("Bucle Arena",15,15,70),
                    Ataque("Disparo lodo",15,55,95),
                    Ataque("Excavar",15,80,100),
                    Ataque("Acido",16,40,100),
                    Ataque("Bomba acida",16,40,100),
                    Ataque("Bomba lodo",16,90,100),
                    Ataque("Carga toxica",16,65,100),
                    Ataque("Cola veneno",16,50,100),
                    Ataque("Colmillo veneno",16,50,100),
                    Ataque("Acrobata",17,55,100),
                    Ataque("Aerochorro",17,100,95),
                    Ataque("Aire Afilado",17,55,95),
                    Ataque("Ascenso draco",17,120,100),
                    Ataque("Ataque aereo",17,140,90),
                    Ataque("Ataque ala",17,60,100)
                   ])

Pokemones = np.array([
    Pokemon("Bulbasaur","Bulbasaur.png",(11,16)),
    Pokemon("Ivysaur","Ivysaur.png",(11,16)),
    Pokemon("Venusaur","Venusaur.png",(11,16)),
    Pokemon("Charmander","Charmander.png",(6,)),
    Pokemon("Charmeleon","Charmeleon.png",(6,)),
    Pokemon("Charizard","Charizard.png",(6,17)),
    Pokemon("Squirtle","Squirtle.png",(1,)),
    Pokemon("Wartortle","Wartortle.png",(1,)),
    Pokemon("Blastoise","Blastoise.png",(1,)),
    Pokemon("Caterpie","Caterpie.png",(2,)),
    Pokemon("Metapod","Metapod.png",(2,)),
    Pokemon("Butterfree","Butterfree.png",(2,17)),
    Pokemon("Weedle","Weedle.png",(2,16)),
    Pokemon("Kakuna","Kakuna.png",(2,16)),
    Pokemon("Beedrill","Beedrill.png",(2,16)),
    Pokemon("Pidgey","Pidgey.png",(10,17)),
    Pokemon("Pidgeotto","Pidgeotto.png",(10,17)),
    #Pokemon("Pidgeot","Pidgeot.png",(10,17)),
    Pokemon("Rattata","Rattata.png",(10,)),
    Pokemon("Raticate","Raticate.png",(10,)),
    Pokemon("Spearow","Spearow.png",(10,17)),
    Pokemon("Fearow","Fearow.png",(10,17)),
    Pokemon("Ekans","Ekans.png",(16,)),
    Pokemon("Arbok","Arbok.png",(16,)),
    Pokemon("Pikachu","Pikachu.png",(4,)),
    Pokemon("Raichu","Raichu.png",(4,)),
    Pokemon("Sandshrew","Sandshrew.png",(15,)),
    Pokemon("Sandslash","Sandslash.png",(15,)),
    Pokemon("NidoranF","NidoranF.png",(16,)),
    Pokemon("Nidorina","Nidorina.png",(16,)),
    Pokemon("Nidoqueen","Nidoqueen.png",(16,15)),
    Pokemon("Nidoran2F","Nidoran2F.png",(16,)),
    Pokemon("Nidorino","Nidorino.png",(16,)),
    Pokemon("Nidoking","Nidoking.png",(16,15)),
    Pokemon("Clefairy","Clefairy.png",(7,)),
    Pokemon("Clefable","Clefable.png",(7,)),
    Pokemon("Vulpix","Vulpix.png",(6,)),
    Pokemon("Ninetales","Ninetales.png",(6,)),
    Pokemon("Jigglypuff","Jigglypuff.png",(10,7)),
    Pokemon("Wigglytuff","Wigglytuff.png",(10,7)),
    Pokemon("Zubat","Zubat.png",(16,17)),
    Pokemon("Golbat","Golbat.png",(16,17)),
    Pokemon("Oddish","Oddish.png",(11,16)),
    Pokemon("Gloom","Gloom.png",(11,16)),
    Pokemon("Vileplume","Vileplume.png",(11,16)),
    Pokemon("Paras","Paras.png",(2,11)),
    Pokemon("Parasect","Parasect.png",(2,11)),
    Pokemon("Venonat","Venonat.png",(2,16)),
    Pokemon("Venomoth","Venomoth.png",(2,16)),
    Pokemon("Diglett","Diglett.png",(15,)),
    Pokemon("Articuno","Articuno.png",(8,17)),
    Pokemon("Zapdos","Zapdos.png",(4,17)),
    Pokemon("Moltres","Moltres.png",(6,17)),
    Pokemon("Dratini","Dratini.png",(3,)),
    Pokemon("Dragonair","Dragonair.png",(3,)),
    Pokemon("Dragonite","Dragonite.png",(3,17)),
    Pokemon("Mewtwo","Mewtwo.png",(12,)),
    #Pokemon("Mew","Mew.png",(12,)),
    Pokemon("Lugia","Lugia.png",(12,17)),
    Pokemon("Entei","Entei.png",(6,)),
    Pokemon("Raikou","Raikou.png",(4,)),
    Pokemon("Suicune","Suicune.png",(1,)),
    Pokemon("Ho-Oh","Ho-Oh.png",(6,17)),
    Pokemon("Celebi","Celebi.png",(12,11)),
    Pokemon("Regirock","Regirock.png",(13,)),
    Pokemon("Regice","Regice.png",(8,)),
    Pokemon("Registeel","Registeel.png",(0,)),
    Pokemon("Kyogre","Kyogre.png",(1,)),
    Pokemon("Groudon","Groudon.png",(15,)),
    Pokemon("Rayquaza","Rayquaza.png",(3,17)),
    Pokemon("Latias","Latias.png",(3,12)),
    Pokemon("Latios","Latios.png",(3,12)),
    Pokemon("Jirachi","Jirachi.png",(0,12))
])


#Asignacion de pokemones a usuario y a maquina
a=np.arange(Pokemones.size)
b=np.arange(Ataques.size)
PokemonesAleatorioUser = np.random.choice(a,3)
PokemonesAleatorioMachine = np.random.choice(a,3)
pokemonesUser=np.array([])
pokemonesMaquina=np.array([])
for i in range(0,3):
    pokemonesUser=np.append(pokemonesUser,Pokemones[PokemonesAleatorioUser[i]])
    ataquesRand = np.random.choice(b,4)
    ataques = np.array([])
    for j in range(0, 4):
        ataques=np.append(ataques,Ataques[ataquesRand[j]])
    pokemonesUser[i].setAtaques(ataques)

for i in range(0,3):
    pokemonesMaquina=np.append(pokemonesMaquina,Pokemones[PokemonesAleatorioMachine[i]])
    ataquesRand = np.random.choice(b,4)
    ataques = np.array([])
    for j in range(0, 4):
        ataques=np.append(ataques,Ataques[ataquesRand[j]])
    pokemonesMaquina[i].setAtaques(ataques)

print(pokemonesUser[0].Nombre,pokemonesUser[1].Nombre,pokemonesUser[2].Nombre,"vs",
      pokemonesMaquina[0].Nombre,pokemonesMaquina[1].Nombre,pokemonesMaquina[2].Nombre,)

#Accion botones
def Action1():
    global indicePokemonMacine
    global indcePokemonUser
    if indcePokemonUser >= 3 or indicePokemonMacine>=3:
        return
    pokemonesMaquina[indicePokemonMacine].takeDamage(pokemonesUser[indcePokemonUser].Ataques[0].Potencia*
                                                     100/pokemonesUser[indcePokemonUser].Ataques[0].Precision*
                                                     multiplicador[pokemonesUser[indcePokemonUser].Ataques[0].Tipo]
                                                                  [pokemonesMaquina[indicePokemonMacine].Tipos[0]])
    if (pokemonesMaquina[indicePokemonMacine].Vida) <= 0:
        indicePokemonMacine+=1;

    if indicePokemonMacine>=3:
        LabelInfo.config(text="Gano el usuario")

        return
    refresh()

    arbol = Arbol(pokemonesUser[indcePokemonUser],pokemonesMaquina[indicePokemonMacine],multiplicador)
    indice = arbol.getDecision()
    pokemonesUser[indcePokemonUser].takeDamage(pokemonesMaquina[indicePokemonMacine].Ataques[indice].Potencia *
                                                     100 / pokemonesMaquina[indicePokemonMacine].Ataques[indice].Precision *
                                                     multiplicador[pokemonesMaquina[indicePokemonMacine].Ataques[indice].Tipo]
                                                     [pokemonesUser[indcePokemonUser].Tipos[0]])
    LabelInfo.config(text="Tu "+pokemonesUser[indcePokemonUser].Nombre+" ha usado "+
                          pokemonesUser[indcePokemonUser].Ataques[0].Nombre+"\n"+
                          pokemonesMaquina[indicePokemonMacine].Nombre + " ha usado " +
                          pokemonesMaquina[indicePokemonMacine].Ataques[indice].Nombre)
    if (pokemonesUser[indcePokemonUser].Vida) <= 0:
        indcePokemonUser+=1;

    if indcePokemonUser>=3:
        LabelInfo.config(text="Gano la maquina")

        return


    refresh()

def Action2():
    global indicePokemonMacine
    global indcePokemonUser
    if indcePokemonUser >= 3 or indicePokemonMacine >= 3:
        return
    pokemonesMaquina[indicePokemonMacine].takeDamage(pokemonesUser[indcePokemonUser].Ataques[1].Potencia *
                                                     100 / pokemonesUser[indcePokemonUser].Ataques[1].Precision *
                                                     multiplicador[pokemonesUser[indcePokemonUser].Ataques[1].Tipo]
                                                     [pokemonesMaquina[indicePokemonMacine].Tipos[0]])
    if (pokemonesMaquina[indicePokemonMacine].Vida) <= 0:
        indicePokemonMacine += 1;

    if indicePokemonMacine >= 3:
        LabelInfo.config(text="Gano el usuario")

        return
    refresh()

    arbol = Arbol(pokemonesUser[indcePokemonUser], pokemonesMaquina[indicePokemonMacine], multiplicador)
    indice = arbol.getDecision()
    pokemonesUser[indcePokemonUser].takeDamage(pokemonesMaquina[indicePokemonMacine].Ataques[indice].Potencia *
                                               100 / pokemonesMaquina[indicePokemonMacine].Ataques[indice].Precision *
                                               multiplicador[pokemonesMaquina[indicePokemonMacine].Ataques[indice].Tipo]
                                               [pokemonesUser[indcePokemonUser].Tipos[0]])

    LabelInfo.config(text="Tu "+pokemonesUser[indcePokemonUser].Nombre+" ha usado "+
                          pokemonesUser[indcePokemonUser].Ataques[1].Nombre+"\n"+
                          pokemonesMaquina[indicePokemonMacine].Nombre + " ha usado " +
                          pokemonesMaquina[indicePokemonMacine].Ataques[indice].Nombre)
    if (pokemonesUser[indcePokemonUser].Vida) <= 0:
        indcePokemonUser += 1;

    if indcePokemonUser >= 3:
        LabelInfo.config(text="Gano la maquina")

        return



    refresh()

def Action3():
    global indicePokemonMacine
    global indcePokemonUser
    if indcePokemonUser >= 3 or indicePokemonMacine >= 3:
        return
    pokemonesMaquina[indicePokemonMacine].takeDamage(pokemonesUser[indcePokemonUser].Ataques[2].Potencia *
                                                     100 / pokemonesUser[indcePokemonUser].Ataques[2].Precision *
                                                     multiplicador[pokemonesUser[indcePokemonUser].Ataques[2].Tipo]
                                                     [pokemonesMaquina[indicePokemonMacine].Tipos[0]])
    if (pokemonesMaquina[indicePokemonMacine].Vida) <= 0:
        indicePokemonMacine += 1;

    if indicePokemonMacine >= 3:
        LabelInfo.config(text="Gano el usuario")

        return
    refresh()

    arbol = Arbol(pokemonesUser[indcePokemonUser], pokemonesMaquina[indicePokemonMacine], multiplicador)
    indice = arbol.getDecision()
    pokemonesUser[indcePokemonUser].takeDamage(pokemonesMaquina[indicePokemonMacine].Ataques[indice].Potencia *
                                               100 / pokemonesMaquina[indicePokemonMacine].Ataques[indice].Precision *
                                               multiplicador[pokemonesMaquina[indicePokemonMacine].Ataques[indice].Tipo]
                                               [pokemonesUser[indcePokemonUser].Tipos[0]])
    LabelInfo.config(text="Tu "+pokemonesUser[indcePokemonUser].Nombre+" ha usado "+
                          pokemonesUser[indcePokemonUser].Ataques[2].Nombre+"\n"+
                          pokemonesMaquina[indicePokemonMacine].Nombre + " ha usado " +
                          pokemonesMaquina[indicePokemonMacine].Ataques[indice].Nombre)
    if (pokemonesUser[indcePokemonUser].Vida) <= 0:
        indcePokemonUser += 1;

    if indcePokemonUser >= 3:
        LabelInfo.config(text="Gano la maquina")

        return



    refresh()

def Action4():
    global indicePokemonMacine
    global indcePokemonUser
    if indcePokemonUser >= 3 or indicePokemonMacine >= 3:
        return
    pokemonesMaquina[indicePokemonMacine].takeDamage(pokemonesUser[indcePokemonUser].Ataques[3].Potencia *
                                                     100 / pokemonesUser[indcePokemonUser].Ataques[3].Precision *
                                                     multiplicador[pokemonesUser[indcePokemonUser].Ataques[3].Tipo]
                                                     [pokemonesMaquina[indicePokemonMacine].Tipos[0]])
    if (pokemonesMaquina[indicePokemonMacine].Vida) <= 0:
        indicePokemonMacine += 1;

    if indicePokemonMacine >= 3:
        LabelInfo.config(text="Gano el usuario")

        return
    refresh()

    arbol = Arbol(pokemonesUser[indcePokemonUser], pokemonesMaquina[indicePokemonMacine], multiplicador)
    indice = arbol.getDecision()
    pokemonesUser[indcePokemonUser].takeDamage(pokemonesMaquina[indicePokemonMacine].Ataques[indice].Potencia *
                                               100 / pokemonesMaquina[indicePokemonMacine].Ataques[indice].Precision *
                                               multiplicador[pokemonesMaquina[indicePokemonMacine].Ataques[indice].Tipo]
                                               [pokemonesUser[indcePokemonUser].Tipos[0]])

    LabelInfo.config(text="Tu " + pokemonesUser[indcePokemonUser].Nombre + " ha usado " +
                          pokemonesUser[indcePokemonUser].Ataques[3].Nombre + "\n" +
                          pokemonesMaquina[indicePokemonMacine].Nombre + " ha usado " +
                          pokemonesMaquina[indicePokemonMacine].Ataques[indice].Nombre)
    if (pokemonesUser[indcePokemonUser].Vida) <= 0:
        indcePokemonUser += 1;

    if indcePokemonUser >= 3:
        LabelInfo.config(text="Gano la maquina")

        return



    refresh()

#Actualizacion de datos y de pantalla
def refresh():
    filenameUser.config(file="Pokemones/"+pokemonesUser[indcePokemonUser].Imagen)
    pokemonImageUser.config(image=filenameUser)
    filenameMachine.config(file="Pokemones/"+pokemonesMaquina[indicePokemonMacine].Imagen)
    pokemonImageMachine.config(image=filenameMachine)

    VidaUser.config(text="Vida: " + str(pokemonesUser[indcePokemonUser].Vida))
    VidaMachine.config(text="Vida: " + str(pokemonesMaquina[indicePokemonMacine].Vida))
    NombreUser.config(text="Nombre: "+pokemonesUser[indcePokemonUser].Nombre)
    NombreMachine.config(text="Nombre: "+pokemonesMaquina[indicePokemonMacine].Nombre)



    Ataque1.config(text =pokemonesUser[indcePokemonUser].Ataques[0].Nombre)
    Ataque2.config(text =pokemonesUser[indcePokemonUser].Ataques[1].Nombre)
    Ataque3.config(text =pokemonesUser[indcePokemonUser].Ataques[2].Nombre)
    Ataque4.config(text =pokemonesUser[indcePokemonUser].Ataques[3].Nombre)


#Inicio de la interfaz
indcePokemonUser = 0
indicePokemonMacine =0

gui = Tk()
gui.title("POKEMON")
gui.resizable(width=False, height=False)
gui.geometry("800x620")
"""
for i in Pokemones:
    filenameUser = PhotoImage(file="Pokemones/" + i.Imagen)
"""
filename = PhotoImage(file = "fondo.png")
background_label = Label(gui, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

NombreUser = Label(gui,text="Nombre: "+pokemonesUser[indcePokemonUser].Nombre)
VidaUser = Label(gui,text="Vida: "+str(pokemonesUser[indcePokemonUser].Vida))
BarraVidaUser = ttk.Progressbar(gui)
filenameUser = PhotoImage(file = "Pokemones/"+pokemonesUser[indcePokemonUser].Imagen)  #Pokemones/Arbok.png
pokemonImageUser = Label(gui, image=filenameUser)
NombreUser.place(x=70,y=250)
VidaUser.place(x=70,y=265)
#BarraVidaUser.place(x=70,y=285,height = 10,w=200)
pokemonImageUser.place(x=70,y=300)
vidaMax=300
VidaUser.config(text="Vida: "+str(pokemonesUser[indcePokemonUser].Vida))
BarraVidaUser.step(pokemonesUser[indcePokemonUser].Vida)

NombreMachine = Label(gui,text="Nombre: "+pokemonesMaquina[indicePokemonMacine].Nombre)
VidaMachine = Label(gui,text="Vida: "+str(pokemonesMaquina[indicePokemonMacine].Vida))
BarraVidaMachine = ttk.Progressbar(gui,maximum=300)
filenameMachine = PhotoImage(file = "Pokemones/"+pokemonesMaquina[indicePokemonMacine].Imagen)
pokemonImageMachine = Label(gui, image=filenameMachine)
NombreMachine.place(x=530,y=10)
VidaMachine.place(x=530,y=25)
#BarraVidaMachine.place(x=530,y=45,height = 10,w=200)
pokemonImageMachine.place(x=530,y=60)

VidaMachine.config(text="Vida: "+str(pokemonesMaquina[indicePokemonMacine].Vida))

BarraVidaMachine.step(pokemonesMaquina[indicePokemonMacine].Vida)

Ataque1 = Button(gui, text =pokemonesUser[indcePokemonUser].Ataques[0].Nombre,command = Action1,height=2,width=20)
Ataque1.place(x=430,y=500)
Ataque2 = Button(gui, text =pokemonesUser[indcePokemonUser].Ataques[1].Nombre,command = Action2,height=2,width=20)
Ataque2.place(x=600,y=500)
Ataque3 = Button(gui, text =pokemonesUser[indcePokemonUser].Ataques[2].Nombre,command = Action3,height=2,width=20)
Ataque3.place(x=430,y=550)
Ataque4 = Button(gui, text =pokemonesUser[indcePokemonUser].Ataques[3].Nombre,command = Action4,height=2,width=20)
Ataque4.place(x=600,y=550)

LabelInfo = Label(gui,text=" ",font=font.Font(size=14))
LabelInfo.place(x=10,y=530)

gui.mainloop()
