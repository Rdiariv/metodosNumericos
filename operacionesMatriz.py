#/usr/bin/python3
#-*- coding: utf-8 -*-
from numpy import *

#pide al usuario el número de variables y genera una matriz aumentada para que el usuario
#introduzca los valores de los coeficientes. Retorna la matriz aumentada
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
        print("---------------------------------------------------")


    print("La matriz aumentada introducida es: ")
    print(matriz)

    return matriz 
#Fin de funcion introduceMatrizCoeficientes()




#Intercambia las filas fo y fd de la matriz matriz. Los valores de fo y fd son los de
#las filas de la matriz según python, esto es 0, 1, 2, 3...
#El cambio lo hace en la matriz introducida como parámetro, la función no tiene retorno

def cambioFila(fo, fd, matriz):
    for i in range((matriz.shape)[1]):  #.shape imprime una tupla (filas, columnas) accedo al número de columnas
        
        temp=matriz[fd,i] #guardo coeficiente de fila destino
        matriz[fd,i]=matriz[fo,i] #copio coeficiente de fila origen en fila destino
        matriz[fo,i]=temp #copio coeficiente guardado en la fila origen
    
    print("---------------------------------------------------")
    print("Se han intercambiado las filas %d y %d." %   (fo+1, fd+1))
    print(matriz)

#Fin de cambio de fila