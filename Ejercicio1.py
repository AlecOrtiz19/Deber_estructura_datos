
"""a. Realizar un programa que permita ingresar varios valores numéricos por teclado (uno a la vez)
el ingreso de números terminará cuando se ingrese el número 0, después el programa deberá
presentar la lista sin elementos repetidos, por último, deberá presentar la suma de esta última
lista sin repetidos. Ejemplo se ingresó la lista de números [1,2,5,8,2,5,9] el programa debe
presentar la siguiente lista sin repetidos [1,2,5,8,9] y la suma de estos elementos es 25."""



lista = []
lista2 = []
sumar = 0


def borrar_numero_repetido():
    for i in range(lista.__len__()):
        if lista[i] not in lista2:
            lista2.append(lista[i])

def agregar_numero():
    while True:
        try:
            num = int(input("Ingrese un numero: "))
            if num != 0:
                lista.append(num)
            else:
                print("FIN")
                break
        except:
            print("INGRESAR UN NUMERO VALIDO")
            
    borrar_numero_repetido()
    
    return lista



agregar_numero()


for i in range(lista2.__len__()):
    sumar += lista2[i]
    
print(f'La lista original es: {lista}')
print(f'La suma de la lista {lista2} es: {sumar}')




