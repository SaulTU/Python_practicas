paises = { 
    "Guatemala": "Ciudad de Guatemala", 
    "El salvador": "San Salvador", 
    "Honduras": "Honduras",
    "Nicaragua": "Managua", 
    "Costa rica": "San Jose", 
    "Panama": "Panama", 
    "Argentina": "Buenos Aires", 
    "Colombia": "Bogota", 
    "Venezuela": "Caracas", 
    "España": "Madrid" 
}

pais = input("Ingrese un pais: ")
#Conviete la primer letra en mayuscula

letra = pais.capitalize() in paises

if(letra==True):
    print(paises[pais.capitalize()])
else:
    print('no existe respuesta')
    print(pais)

'''
if pais in diccionario_capitales:
    capital = diccionario_capitales[pais]
    print(f"La capital de {pais} es {capital}.")
else:
    print(f"No se encontró la capital del país {pais}.")
'''