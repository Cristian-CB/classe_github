lista = [9,3,2,5,1]


def ordenar (lista):
    n = len(lista)
    print(n)
    for i in range (n):
        for j in range(n-1):

            if (lista [j] > lista[j+1]):
                temporal = lista[j+1]
                lista[j+1]=lista[j]
                lista[j]=temporal
                print("i" , i)
                print("j" ,j)
                print("hola")








ordenar(lista)
print(lista)