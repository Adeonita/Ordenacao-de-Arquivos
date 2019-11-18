import pandas as pd
import numpy as np
import time
import timeit

arquivo = pd.read_csv('dados2.csv', sep=";")

#############################
#QUIK SORT
inicio = timeit.default_timer()
crescente_acession_quickSort = arquivo.sort_values( by='Acession', ascending=True, inplace=False, kind='quicksort', na_position='last')
fim = timeit.default_timer()
print("O tempo de execução da função quickSort ascendente no campo ACESSION foi de:{} ".format(fim - inicio))

inicio = timeit.default_timer()
decrescente_acession_quickSort = arquivo.sort_values( by='Acession', ascending=False, inplace=False, kind='quicksort', na_position='last')
fim = timeit.default_timer()
print("O tempo de execução da função quickSort descendente no campo ACESSION foi de: {}".format(fim - inicio))

inicio = timeit.default_timer()
crescente_date_quickSort = arquivo.sort_values( by='Date', ascending=True, inplace=False, kind='quicksort', na_position='last')
fim = timeit.default_timer()
print("O tempo de execução da função quickSort ascendente no campo DATE foi de: {} \n".format(fim - inicio))

####################################
#MERGE SORT

inicio = timeit.default_timer()
crescente_acession_mergesort = arquivo.sort_values( by='Acession', ascending=True, inplace=False, kind='mergesort', na_position='last')
fim = timeit.default_timer()
print("O tempo de execução da função mergesort ascendente no campo ACESSION foi de: {}".format(fim - inicio))

inicio = timeit.default_timer()
decrescente_acession_mergesort = arquivo.sort_values( by='Acession', ascending=False, inplace=False, kind='mergesort', na_position='last')
fim = timeit.default_timer()
print("O tempo de execução da função mergesort descendente no campo ACESSION foi de: {}".format(fim - inicio))

inicio = timeit.default_timer()
crescente_date_mergesort = arquivo.sort_values( by='Date', ascending=True, inplace=False, kind='mergesort', na_position='last')
fim = timeit.default_timer()
print("O tempo de execução da função mergesort ascendente no campo DATE foi de: {} \n".format(fim - inicio))

###############################
#HEAP SORT

inicio = timeit.default_timer()
crescente_acession_heapsort = arquivo.sort_values( by='Acession', ascending=True, inplace=False, kind='heapsort', na_position='last')
fim = timeit.default_timer()
print("O tempo de execução da função heapsort ascendente no campo ACESSION foi de: {}".format(fim - inicio))

inicio = timeit.default_timer()
decrescente_acession_heapsort = arquivo.sort_values( by='Acession', ascending=False, inplace=False, kind='heapsort', na_position='last')
fim = timeit.default_timer()
print("O tempo de execução da função heapsort descendente no campo ACESSION foi de: {}".format(fim - inicio))

inicio = timeit.default_timer()
crescente_date_heapsort = arquivo.sort_values( by='Date', ascending=True, inplace=False, kind='heapsort', na_position='last')
fim = timeit.default_timer()
print("O tempo de execução da função heapsort cendente no campo DATE foi de: {}".format(fim - inicio))



