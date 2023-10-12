
"""Realizar un programa que permita ingresar una frase por teclado y muestre cuantas vocales
tiene la frase ingresada. Adicional después debe presentar la frase ingresada en la cual las
vocales deben estar en mayúscula y las consonantes en minúsculas. Ejemplo. De la frase
“Universidad estatal de milagro” el resultado mostrado seria: La frase cuenta con 12 vocales.
“UnIvErsIdAd EstAtAl dE mIlAgrO”"""

def ingresar_frase(frase):
    vocales = "aeiouAEIOU"
    contador = 0
    resultado = ""
    for i in frase:
        if i in vocales:
            resultado += i.upper()
            contador +=1
        else:
            resultado += i.lower()
            
    print(f"La frase cuenta con {contador} vocales: {resultado}")
    print(resultado)


frase = input("Ingrese una frase: ")

ingresar_frase(frase)


