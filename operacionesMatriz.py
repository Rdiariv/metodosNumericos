#/usr/bin/python3
#-*- coding: utf-8 -*-
from numpy import *

def introduceMatrizCoeficientes():
    print("Introducir matriz de coeficientes.\n")
    
    #Pido número de incognitas al usuario y preparo los datos
    dimension=input("Introduzca número de incognitas: ")
    print('El número de ecuaciones es '+dimension+'.\n')
    dimension=int(dimension)
    filas=dimension
    columnas=dimension+1
    #Creo matriz aumentada
    matriz=zeros((filas,columnas))

    #Pido valores de coeficientes para la matriz aumentada
    for i in range(filas):
        print("Ecuación %d" %   (i+1))
        print("---------------------------------------------------")
        for j in range(columnas-1):
            matriz[i,j]=input("Coeficiente %d:"  %   (j+1))
        matriz[i,columnas-1]=input("Introduzca coeficiente ecuación %d: " %   (i+1))
        print("\nEcuación %d:  " % (i+1))
        print(matriz[(i),:])
        print("---------------------------------------------------\n\n")


    print("La matriz aumentada introducida es: ")
    print(matriz)

    return matriz 
#Fin de funcion introduceMatrizCoeficientes()


