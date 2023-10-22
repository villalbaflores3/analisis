import pandas as pd
# En el archivo mis_matematicas.py


def convertirNumero(valor):
    try:
        numero = int(valor)      
        return numero    
    except ValueError:
        return pd.NA


class Calculadora:
    def __init__(self):
        self.valor = 0




