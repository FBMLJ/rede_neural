import numpy as np
import random
import math
def sigmoid(number):
    return np.array([1/(1 + math.exp(-i)) for i in number])

class Camada:
    def __init__(self, anterior,entrada, camadas, saida_final):
        self.anterior = anterior
        if anterior != None:
            anterior.proximo = self 
        self.entrada = entrada
        
        if camadas != 1:
            self.camada = np.random.uniform(-1,1, (entrada, entrada)) 
            self.final = False
        else:
            self.camada = np.random.uniform(-1,1, (saida_final, entrada)) 
            self.final = True
            self.proximo = None
        camadas -= 1
        if camadas >= 1:
            Camada(self, entrada, camadas, saida_final) 
    
    def predict(self, entrada):
        if self.final == False:
            return self.proximo.predict(self.operacao(entrada))
        return self.operacao(entrada)

    def operacao(self, entrada):
        return sigmoid(np.dot(self.camada, entrada))