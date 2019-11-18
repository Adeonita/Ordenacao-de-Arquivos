import pandas as pd
import numpy as np
import time
import timeit

arquivo = pd.read_csv('dados2.csv', sep=";")

inicio = timeit.default_timer()
crescente_acession_quickSort = arquivo.sort_values( by='Acession', ascending=True, inplace=False, kind='quicksort', na_position='last')
fim = timeit.default_timer()
print("O tempo de execução da função quickSort ascendente no campo ACESSION foi de:{} ".format(fim - inicio))

inicio = timeit.default_timer()
decrescente_acession_quickSort = arquivo.sort_values( by='Acession', ascending=False, inplace=False, kind='quicksort', na_position='last')
fim = timeit.default_timer()
print("O tempo de execução da função quickSort descendente no campo ACESSION foi de: {}".format(fim - inicio))

inicio = timeit.default_timer()
decrescente_date_quickSort = arquivo.sort_values( by='Date', ascending=False, inplace=False, kind='quicksort', na_position='last')
fim = timeit.default_timer()
print("O tempo de execução da função quickSort descendente no campo DATE foi de: {}".format(fim - inicio))
print(' \n')