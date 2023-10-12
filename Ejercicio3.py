
""""Dada el siguiente arreglo [4,6,9,88,45,52,15,65,78] realizar el ordenamiento empleando el
método de la burbuja, el arreglo debe ser ordenado de manera ascendente (de menor a
mayor). Nota este ejercicio deberá realizarlo empleando programación orientada a objetos."""


class Burbuja:
    def __init__(self, arreglo):
        self.arreglo = arreglo

    def ordenamiento_burbuja(self):
        band = False
        while band == False:
            band = True
            for i in  range(len(self.arreglo) -1 ):
                if self.arreglo[i] > self.arreglo[i+1]:
                    auxiliar = self.arreglo[i]
                    self.arreglo[i] = self.arreglo[i+1]
                    self.arreglo[i+1] = auxiliar
                    band = False
                    
        print(f'Arreglo ordenado: {self.arreglo}')

ordenamiento = Burbuja([4,6,9,88,45,52,15,65,78])
ordenamiento.ordenamiento_burbuja()