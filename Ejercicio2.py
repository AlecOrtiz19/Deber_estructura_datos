

"""Realizar un programa que permita ingresar 5 valores numéricos primos por teclado (uno a la
vez), presentar el número mayor, el menor y el intermedio."""


lista1 = []

def validar_numero():
    while True:
        try:
            numero = int(input("Ingrese un numero primo: "))
            if numero > 1:
                break
            else:
                print("No es un numero primo..")
        except:
            print("Dato no valido")
    return numero

def max_min_intermedio(arreglo):
    valorMaximo = arreglo[0]
    valorMinimo = arreglo[0]
    
    for i in range(len(arreglo)):
        if  arreglo[i] > valorMaximo:
            valorMaximo = arreglo[i]

        if arreglo[i] < valorMinimo:
            valorMinimo = arreglo[i]
    suma = valorMaximo + valorMinimo
    print(f'El valor maximo es: {valorMaximo}')
    print(f'El valor minimo es : {valorMinimo}')
    print(f'El intermedio es:  {suma//2}' )

    
def agregar_numero_primo():

    while True:
        num = validar_numero()
        
        if num > 1:
            i = 2
            contador = 0
            while i < num and contador == 0:
                resto = num % i
                
                if resto == 0:
                    print("No es un numero primo..")
                    contador +=1
                
                i += 1
                
            if contador == 0:
                lista1.append(num)
                    
            if lista1.__len__() == 5:
                print(lista1)
                break
                    
        else:
            print("No es un numero primo")
            
    max_min_intermedio(lista1)
    
    



agregar_numero_primo()


