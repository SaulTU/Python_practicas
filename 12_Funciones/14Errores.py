while True:
    try:
        edad = int(input("Ingrese su edad: "))
        print("Tu edad es: ",edad)
        break
    except:
        print("Ingresaste un valor erroneo")
    finally:
        print("La ejecucion ha finalizado")

while True:
    try:
        edad = int(input("Ingrese su edad: "))
        print("Tu edad es: ",edad)
        break
    except ValueError:
        print("Ingresaste un valor erroneo")
    except KeyboardInterrupt:
        print("Cancelaste la ejecucion")
        break
    finally:
        print("La ejecucion ha finalizado")