import random

class Reflector():
    
    __español = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    
    def __init__(self, alfabeto=__español):
        self.abecedario = self.__español
        self.reflector = []
        listAbecedario = list(self.abecedario)
        for i in self.abecedario:
            if i not in listAbecedario:
                continue
            j = random.choice(listAbecedario)  
            
            while i == j:
                j = random.choice(listAbecedario)
                if len(listAbecedario) == 1:
                    break
            self.reflector.append([i,j])
            #print(i,j)
            if i in listAbecedario:
                listAbecedario.remove(i)
            if j in listAbecedario:
                listAbecedario.remove(j)
            
            #print(listAbecedario, len(listAbecedario))
            if listAbecedario == []:
                break



