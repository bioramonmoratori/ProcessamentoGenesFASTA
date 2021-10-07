# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 16:27:47 2021

@author: ramon
"""

#PROCESSAMENTO DE ARQUIVOS GENOMICOS FASTA 

import numpy as np
import pandas as pd
import csv

#################################################################################

#Abre o arquivo contendo o genoma FASTA e salva em uma lista de strings chamada 'arquivoprocessado'

arquivotxt = open('C:/Users/ramon/Desktop/CienciaDeDados/Prototipos/ProcessamentoFASTA/cromossomo19.txt', 'r')

arquivopreprocessado = str(arquivotxt.readlines())

#print(arquivopreprocessado)    
arquivoprocessado = list(arquivopreprocessado)
arquivoprocessado.append('A') #Adiciono uma letra no final para ser possivel dividir em codons de 3
arquivoprocessado.append('A') #Adiciono uma letra no final para ser possivel dividir em codons de 3

#Preciso retirar da lista 'arquivoprocessado' todos os simbolos que nao correspondem aos nucleotideos

for i in range(0, len(arquivoprocessado)):
    if(arquivoprocessado[i] != 'A' and arquivoprocessado[i] != 'T' and arquivoprocessado[i] != 'C' and arquivoprocessado[i] != 'G' and arquivoprocessado[i] != 'U'):
        arquivoprocessado[i] = '0'
        
    if(arquivoprocessado[i] == 'T'):
        arquivoprocessado[i] = 'U'
        
        
while '0' in arquivoprocessado: 
    arquivoprocessado.remove('0')
    
  

print(arquivoprocessado)
print(len(arquivoprocessado))

#################################################################################

#Separar Genoma em Codons

genoma = np.array(arquivoprocessado)
codons = np.split(genoma, len(arquivoprocessado)/3) #Pego o numero de nucleotideos e formo grupos de 3


#Salvo os codons em um csv
converter = pd.DataFrame(codons)
converter.to_csv('genomacodons.csv', index=False, header=False)


