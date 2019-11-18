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


def sort_decendente(lines):

      
    sort_decrescente = []
    maior = ''
    
    for line in lines:
        if( maior == '' ):
            maior = line[0]
        elif( maior > line[0]):
            maior = line[0]
        
           

    return (sort_decrescente)

    

crescente = sort_ascendente(lines)
decrescente = sort_decendente(lines)
        
        
    