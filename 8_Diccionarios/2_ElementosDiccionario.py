diccionario = {
    'Nombre' : 'Saul', 
    'Apellido': 'Torres', 
    'Estatura': 1.62
}

print(diccionario)
print(type(diccionario))
print(diccionario.keys())
print(diccionario.values())

print(diccionario['Estatura'])

diccionario['Peso'] = '60 kg'
print(diccionario)

diccionario['Peso'] = '58 kg'
print(diccionario)

