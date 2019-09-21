class Pokemon:

    def __init__(self,nombre,imagen,tipos):
        self.Nombre = nombre
        self.Vida = 300
        self.Imagen = imagen
        self.Tipos = tipos

    def setAtaques(self,ataques):

        self.Ataques = ataques

    def takeDamage(self,dano):
        self.Vida-=dano




