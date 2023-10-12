

"""Realizar un programa que permita ingresar una frase por teclado, después el programa pide el
ingreso de dos índices (inicio y fin), por ultimo el programa debe presentar los caracteres que
se encuentran entre esos índices. Ejemplo se ingresa la frase “Facultad de Ciencia e
Ingenieria” y los índices que ingresa de inicio es el 4 y el de fin es el 9 lo que debe presentar
como resultado es “ltad d”"""

frase = ""

def validar_numero(texto):
    
    while True:
        try:
            numero = int(input(f"Ingrese el {texto}: "))
            
            if numero > len(frase):
                print(f"Ingrese el {texto} correcto")
            else:
                break
                
        except:
            print("Dato no valido")
            
    return numero

def inicio_fin(palabra,inicio,fin):
    frase_1 = palabra
    n1 = inicio
    n2 = fin
    
    print(f"El inicio es {n1} el fin es {n2} y el resultado es: {frase_1[inicio:fin + 1]}")
            
    
frase = input("Ingrese una frase: ")
inicio = validar_numero("inicio")
fin = validar_numero("fin")
inicio_fin(frase, inicio, fin)


