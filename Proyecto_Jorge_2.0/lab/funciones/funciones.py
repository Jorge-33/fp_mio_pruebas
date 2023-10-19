'''
Created on 15 oct 2023

@author: Jorge-Feo
'''
from cmath import sqrt
"""
Ejercicio 1
"""
def es_primo(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

n = int(input("Inserte un número entero y positivo: "))

if es_primo(n):
    print("El {} es un número primo".format(n))
else:
    print("El {} no es un número primo".format(n))
"""
Ejercicio 2
"""
from math import factorial
def num_combinatorio(n,k):
    if n >= k:
        return factorial(n)//(factorial(k)*factorial(n-k))
    else:
        return("n debe ser mayor a k para poder realizar la operación")
n= int(input("Inserte el primer número entero, siendo el primero mayor que el segundo: "))   
k= int(input("Inserte el segundo número entero, siendo el primero mayor que el segundo: "))  
print ("El resultado del numero combinatorio de {} y {} es {}".format(n,k,num_combinatorio(n,k)))
        
"""
Ejercicio 3
"""       
def funcion_S(n,k):
    if n >= k:
        resultado = 0
    
        for i in range(k+1):
            resultado += ((-1) ** i) * num_combinatorio(k,i) * (2 ** (k - i)) * factorial(k - i)
    
            return (1 / factorial(k)) * resultado
    else:
        return("n debe ser mayor a k para poder realizar la operación")
n= int(input("Inserte el primer número entero, siendo el primero mayor que el segundo: "))   
k= int(input("Inserte el segundo número entero, siendo el primero mayor que el segundo: "))
"""
Ejercicio 4
"""
def dif_num_lista(lista):
    for i in range (0, len(lista)):
        lista[i]= abs(lista[i]-lista[i+1])
    return lista
lista=input("Introduzca la lista a Continuación: ")
"""
Ejercicio 5
"""
def cadena_mas_larga(lista_cadenas):
    if not lista_cadenas:
        return None
    
    cadena_mas_larga = lista_cadenas[0]
    
    for cadena in lista_cadenas:
        if len(cadena) > len(cadena_mas_larga):
            cadena_mas_larga = cadena
    
    return cadena_mas_larga
lista_cadenas=input("Introduzca la lista a Continuación: ")

"""
parte nueva
"""
def funcion_A(n:int,k:int,i:int=0):
    if k>=i>=0:
        p =(n-i)**2
        resultado=0
        for i in range (0, k):
            resultado*=p
            return resultado
    else:
        return(f"[k] no es mayor que [i] o [i] no es mayor que 0")
def num_combinatorio_2(n:int,k:int):
    if (n+1) >=k:
        return factorial(n)//(factorial(k)*factorial(n-k))
    else:
        return(f"[n+1] no es mayor que [k]")
def funcion_S2(n:int,k:int):
    if n>=k>=0:
        resultado=0
        for i in range(0,k+1):
            resultado+=((-1)**i)*num_combinatorio(k, i)*((k-i)**n)
            return resultado*(factorial(k)/sqrt(k))
    else:
        return(f"[n]no es mayor o iguAL QUE [k] o [k] no es myor o igual a cero")

