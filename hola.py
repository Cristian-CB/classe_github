import random

def ordenar_burbuja (lista):
    n = len(lista)
    for i in range (n):
        for j in range(n-1):
            if (lista [j] > lista[j+1]):
                temporal = lista[j+1]
                lista[j+1]=lista[j]
                lista[j]=temporal

lista = [random.randint(1,100) for i in range(50)]

print(lista)
ordenar_burbuja(lista)
print(lista)