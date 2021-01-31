#VERSION PREELIMINAR 
# MÁQUINA BÁSICA: UN ROTOR (ALEATORIO) Y UN REFLECTOR
# REPRODUCE EL CONCEPTO DE LA MÁQUINA ENIGMA  

import random
from rotor import *
from reflector import *


class Maquina():
         

    def __init__(self):
        self.ro = Rotor()
        self.re = Reflector()
        self.codigoIda = '' 
        self.reflejo = ''  #primer elemento de un par en el reflector
        self.codigoVuelta = ''   #segundo elemento de un par en el reflector
        self.cadenaCodificada = ''
        self.posBombilla = 0
        self.bombilla = ''

    def conexion(self):  #funcion que conecta el rotor con el reflector
       
        for i in range(len(self.re.reflector)):
            if self.re.reflector[i][0] == self.codigoIda:     
                self.reflejo = self.re.reflector[i][1]
                break
            if self.re.reflector[i][1] == self.codigoIda:
                self.reflejo = self.re.reflector[i][0]
                break
        return self.reflejo


    def vuelta(self):  #función que decodifica el reflejo enviado por el reflector
        for i in self.ro.rotorC:
            if i == self.reflejo:
               self.codigoVuelta = i
               self.posBombilla = self.ro.rotorC.index(self.codigoVuelta)
               self.bombilla = self.ro.abecedario[self.posBombilla]     

    def codificaLetra(self, letra):
       self.codigoIda = self.ro.ida(letra) #devuelve el codigo de ida en el rotor
       self.conexion()  #devuelve el reflejo del código de ida en el reflector
       self.vuelta() #devuelve la letra codificada en la bombilla
       return self.bombilla

    def codifica(self):  #falta validar entradas
        self.ro.posicionInicial(0)
        cadena = input("Introduce cadena: ")
                      
        for letra in cadena:
            self.codificaLetra(letra)
            self.cadenaCodificada += self.bombilla
        print(self.cadenaCodificada)
        self.cadenaCodificada =''
            
        
        

if __name__ =="__main__": 
        ma = Maquina()
        ma.codifica()
        print(ma.ro.rotorC)
        ma.codifica()

        

        
       
