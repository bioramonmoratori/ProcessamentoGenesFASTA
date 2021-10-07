# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 22:58:06 2021

@author: ramon
"""

#Definindo o tipo de aminoacido que compoe cada codon do genoma pre-processado

import pandas as pd
import csv
import numpy as np
from sklearn.model_selection import train_test_split #Divide os dados em treino e teste
from sklearn.preprocessing import LabelEncoder #Para transformar dados categoricos em numericos
from sklearn.metrics import confusion_matrix, accuracy_score #Utilizo matrizes de confusao
from sklearn.ensemble import RandomForestClassifier

#################################################################################

#importo o csv dos codons pre-processados
genoma = pd.read_csv('tiposdecodons.csv', sep=';')

print(genoma.head(10)) #Exibo os primeiros 10 elementos da lista

#################################################################################


categorias = genoma.iloc[:,0:1].values #Pego todas as linhas e colunas de 0 a 0 e transformo em matriz
classes = genoma.iloc[:,1] #Pego todas as linhas da coluna 1 e transformo em matriz

labelencoder1 = LabelEncoder()
categorias[:,0] = labelencoder1.fit_transform(categorias[:,0])


#################################################################################

#Agora vamos dividir os dados entre treino e teste
#Dividiremos em 70% dos dados para treino e 30% para teste

#X sao os dados das categorias e Y os dados daquilo que eu desejo prever
x_treinamento, x_teste, y_treinamento, y_teste = train_test_split(categorias, 
                                                                  classes, 
                                                                  test_size = 0.6,
                                                                  random_state = 0)

print(x_teste)
print(y_teste)


################################################################################

#Vamos criar e treinar o modelo Random Forest

floresta = RandomForestClassifier(n_estimators = 100) #Decidimos o numero de arvores aleatorias a serem criadas
floresta.fit(x_treinamento, y_treinamento) #Para criar o modelo, vamos usar os dados de treinamento

################################################################################

#Agora podemos testar o modelo na pratica

previsao = floresta.predict(x_teste) #Usamos os dados das categorias do teste

print(previsao)

################################################################################

#Agora vamos analisar a taxa de erros e acertos do modelo, atraves da matriz de confusao

confusao = confusion_matrix(y_teste, previsao)
print(confusao)

#Utilizamos tambem o accuracy para determinar a taxa de acerto
taxa_acerto = accuracy_score(y_teste, previsao)
taxa_erro = 1 - taxa_acerto

print(taxa_acerto)

################################################################################

# Aplicando o modelo no genoma humano do cromossomo 19

dadosnovos = pd.read_csv('tiposdecodons.csv', sep=';')

print(dadosnovos.head(10))

################################################################################

categoriasnovas = dadosnovos.iloc[:,0:1].values #Pego todas as categorias da coluna 0 a 0

#Reutilizo os LabelEncoders utilizados anteriormente
categoriasnovas[:,0] = labelencoder1.fit_transform(categoriasnovas[:,0])

#Uso o modelo Random Forest para fazer a predicao das novas categorias

resultado = floresta.predict(categoriasnovas) 
print(resultado)

################################################################################

#Salvando a nova sequencia em uma lista

#Salvo os codons em um csv
converter = pd.DataFrame(resultado)
converter.to_csv('genomaaminoacidos.csv', index=False, header=False)
