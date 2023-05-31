lista = [1,2,3,4,5,6,7,8]
lista1 = []
lista2 = []
def agregar():
    a = int(input("Agregar"))
    lista.append(a)

agregar()

def separar():
    for i in lista:
        if i%2==0:
            lista1.append(i)
        else:
            lista2.append(i)

separar()
print(lista1)
print(lista2)