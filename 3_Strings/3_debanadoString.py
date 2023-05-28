from cgi import print_form


cadena = "Ejemplo de subString (debanado de cadena)"

print(len(cadena)) #tamaño de cadena
print(cadena[0])
print(cadena[2])
#dos formas mismo resultado
print(cadena[0:10])
print(cadena[:10])
#de la posicion indicada en adelante
print(cadena[10:])
#sustrae de derecha a izquierda
print(cadena[-10:])