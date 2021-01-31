import random
from enigma02 import *

#----------------pruebas rotor:

rotor_pruebas = ['W', 'U', 'S', 'Q', 'N', 'F', 'Ñ', 'G', 'M', 'C', 'J',
 'D', 'Y', 'I', 'X', 'L', 'B', 'H', 'A', 'V', 'R', 'P', 'E', 'T', 'O', 'K', 'Z']

#r=Rotor()
#r.rotor = rotor_pruebas
#r.rotorC = r.rotor[:]

#r.posicionInicial('S')
#print(r.rotorC)
#print(r.codifica('H'), "\n", r.rotorC)
#print(r.codifica('O'), "\n", r.rotorC)
#print(r.codifica('L'), "\n", r.rotorC)
#print(r.codifica('A'), "\n", r.rotorC)

#----------------pruebas reflector:

reflector_pruebas = [('A', 'S'), ('C', 'X'), ('D', 'T'),
('E', 'V'), ('F', 'M'), ('G', 'Y'), ('H', 'Z'), ('I', 'P'),
 ('J', 'Q'), ('K', 'L'), ('N', 'Ñ'), ('O', 'U'), ('R', 'B'), ('W', 'W')]


#print(re.reflector)


#----------------pruebas máquina:

ma = Maquina()
ma.ro.rotor = rotor_pruebas
ma.ro.rotorC = rotor_pruebas
ma.re.reflector = reflector_pruebas
print(ma.codifica('EXGCUUJOS'))
print(ma.ro.rotorC)

