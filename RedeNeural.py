import numpy as np
import Camada
class RedeNeural:
    def __init__(self, tamanho_entrada, numero_de_saida, numero_de_camada):
        self.tamanho_entrada = tamanho_entrada
        self.numero_de_camada = numero_de_camada
        self.numero_de_saida = numero_de_saida
        self.primeira_camada = Camada.Camada(None, tamanho_entrada, numero_de_camada -1 , numero_de_saida)
    
    def predict(self, entrada):
        return self.primeira_camada.predict(entrada)