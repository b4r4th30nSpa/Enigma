

#abecedario
abecedario = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#juego de rotores  
juego = {'I'  : ['EKMFLGDQVZNTOWYHXUSPAIBRCJ', 'Q'],
            'II' : ['AJDKSIRUXBLHWTMCQGZNPYFVOE' , 'E'],
            'III': ['BDFHJLCPRTXVZNYEIWGAKMUSQO' , 'V'],
            'IV' : ['ESOVPZJAYQUIRHXLNFTGKDCMWB' , 'J'],
            'V'  :  ['VZBRGITYUPSDNHLXAWMJQOFECK', 'Z'],
            'VI' : ['JPGVOUMFYQBENHZRDKASXLICTW', 'ZM'],
            'VII': ['NZJHGRCXMYSWBOUFAIVLPEKQDT', 'ZM'],
            'VIII': ['FKQHTLXOCBJSPDZRAMEWNIUYGV', 'ZM']
            }
#juego de reflectores (UKW):
B =  'YRUHQSLDPXNGOKMIEBFZCWVJAT'
C = 'FVPJIAOYEDRZXWGCTKUQSBNMHL'

class Reflector():
 
    def __init__(self, abecedario, UKW):
        self.abecedario = abecedario
        self.UKW = UKW
        
    def refleja(self,indice): 
        reflejo = self.UKW[indice]
        indice = self.abecedario.index(reflejo)
        return indice

class Rotor():

   
    def __init__ (self, abecedario, pareo, paso='Z', orden =1):
        self.abecedario = abecedario
        self.pareo = pareo
        self._paso = paso    
        self._ini = 0
        self.orden = orden
        


    def ini(self, letra):
        self._ini = self.abecedario.index(letra)

        
    def avanza(self):        
        
        if self.orden == 1:       
            self._ini = (self._ini + 1) % len(self.abecedario)

        if self.orden == 2:  
            if trigger == True:
                self._ini = (self._ini + 1) % len(self.abecedario)
           
        if self.orden == 3:
            if trigger == True:
                self._ini = (self._ini + 1) % len(self.abecedario)
                


    def paso(self):      #TRIGGER CAMBIA A TRUE UN PASO ANTES QUE EL UNIVERSAL SIMULATOR. POR TANTO, DECODIFICA BIEN LA CADENA ANTES Y DESPUÉS DEL PASO PERO NO DECODIFICA BIEN LA LETRA DEL PASO
        if self._ini == self.abecedario.index(self._paso):  
           
            return True 
        else:
            return False                  

    def codifica(self,indice):
      
        indice =  (indice + self._ini) % len(self.abecedario)
        letra = self.pareo[indice]
        indice = (self.abecedario.index(letra) - self._ini) % len(self.abecedario)  
        return indice
        
    def decodifica(self, indice):
        indice =  (indice + self._ini) % len(self.abecedario)
        letra = self.abecedario[indice]
        indice = (self.pareo.index(letra) - self._ini) % len(self.abecedario)  
        return indice 


class Enigma():

   
    def __init__(self, abecedario, rotores, reflector, ini='AAA'):
        self.abecedario = abecedario
        self.rotores = rotores
        self.reflector = reflector
        self.ini = ini 

    def pos_ini(self):
        for i in range(len(self.rotores)):
            self.rotores[i]._ini = self.abecedario.index(self.ini[i])
         

    def codificaCadena(self, cadena):
        cadenaCodificada = ''
        global trigger
        trigger = False
        
        for letra in cadena:
            indice = self.abecedario.index(letra)
            
            for rotor in self.rotores:
                rotor.avanza()
                trigger = rotor.paso()               
                print(trigger)    
                   
                indice = rotor.codifica(indice)
           
            indice = self.reflector.refleja(indice)
            
            for rotor in self.rotores[::-1]:
                indice = rotor.decodifica(indice)

            cadenaCodificada += self.abecedario[indice] 
        print(cadenaCodificada)
        return cadenaCodificada  


reflector = Reflector(abecedario, B)
rotor_1 = Rotor(abecedario, juego['I'][0], juego['I'][1], orden =1)
rotor_2 = Rotor(abecedario, juego['I'][0], juego['I'][1], orden = 2)
rotor_3 = Rotor(abecedario, juego['I'][0], juego['I'][1], orden = 3)

e = Enigma(abecedario, [rotor_1,rotor_2,rotor_3], reflector, ini='AAA')

e.pos_ini()  
e.codificaCadena('ABCEDEFGHIJKLMNOPQRSTUVWXYZ')
e.pos_ini()  
e.codificaCadena('UWDDNNAAWYSTCIRLYBTZXRAAHAN')

    