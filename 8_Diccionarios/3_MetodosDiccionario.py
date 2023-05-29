diccionario = {1:2,2:3,3:4}
diccionario2= {4:5,5:6}
print(diccionario)
#elimina la llave y su valor
diccionario.pop(3)
print(diccionario)
#Da el valor de la llave 
print(diccionario.get(2))
#Crea una nueva llave
diccionario.setdefault(4,8)
print(diccionario)
#Agrega datos de un segundo diccionario
diccionario.update(diccionario2)
print(diccionario)
#genera copia de diccionario
diccionario.copy()
print(diccionario)

#limpia el dicionario
diccionario.clear()
print(diccionario)