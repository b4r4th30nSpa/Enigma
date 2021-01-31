import random

class Rotor():

    __español = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    __english = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self, alfabeto=__español):
        self.abecedario = self.__español
        self.rotor = []
        otrasLetras = list(self.abecedario)
        for i in self.abecedario: 
            n = random.randrange(len(otrasLetras))
            self.rotor.append(otrasLetras[n])
            otrasLetras.pop(n)
        self.rotorC = self.rotor[:]
        

    def ida(self, letra):
        self.avanza()
        posicion = self.abecedario.index(letra)
        codigoIda = self.rotorC[posicion]
        return codigoIda
        
        #raise ValueError("{} no pertenece al abecedario".format(letra))


    def posicionInicial(self, posIni=0):
        self.rotorC = self.rotor[posIni:] + self.rotor[:posIni]
    
    def avanza(self):
        self.rotorC = self.rotorC[1:] + self.rotorC[0:1]
        
