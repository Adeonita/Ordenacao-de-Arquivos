import pandas as pd
import numpy as np

arquivo = pd.read_csv('dados2.csv', sep=";")
tam_arquivo =  len(arquivo)


lines = arquivo.values
sort_decrescente = []

def sort_ascendente(lines):
    
    menor = 'AAAAAAAA'   
    sort_crescente = []

    for line in lines:
        if(line[0] > menor): #Se a linha for maior que o menor
            menor = line[0]  #Então a linha é o proximo menor
            sort_crescente.append(line) #Acrescento na lista de menores
    return (sort_crescente)


        
crescente = sort_ascendente(lines)
print(crescente)
        
        
    