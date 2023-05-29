jugador = {
    1 : "Casillas",     15 : "Ramos",
    3 : "Pique",        5 : "Puyol",
    11 : "Capdevila",   14 : "Xabi Alonso",
    16 : "Busquets",    8 : "Xavi Hernandez",
    18 : "Pedrito",     6 : "Iniesta",
    7 : "Villa"
}
numero = int(input("Ingrese un numero: "))

if(jugador[numero]):
    print(jugador[numero])
else:
    print('no existe respuesta')
