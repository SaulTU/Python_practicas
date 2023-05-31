from unittest import result


while True:
    try:
        num = int(input("Ingrese un numero: "))
        resultado = 100/num
        print("Tu reswultado es: ",resultado)
        break
    except ZeroDivisionError:
        print("No se puede dividir entre cero")
    finally:
        print("La ejecucion ha finalizado")