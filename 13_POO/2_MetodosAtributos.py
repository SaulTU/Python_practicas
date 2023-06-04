class FabricaTelefonos():
    marca = 'Huawei'
    color = 'negro'
    memoriaRam = 32
    almacenamiento =128

    def llamar(self, mensaje):
        return mensaje

    def escucharMusica(self):
        print('Escuchando Musica')

telefono = FabricaTelefonos()
print(telefono.marca)

print(telefono.llamar("Hola"))

telefono.escucharMusica()