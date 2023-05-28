PESO_Payaso = 112 #gramos
PESo_Muneca = 75 #gramos

payasos = input("ingrese el numero de payasos que desea ")
munecas = input("ingrese el numero de muñecas que desea ")

total_payasos = int(payasos) * PESO_Payaso
total_munecas = int(munecas) * PESo_Muneca
total = total_payasos + total_munecas
print('suma payasos ' + str(total_payasos))
print('suma muñecas ' + str(total_munecas))
print('suma total ' + str(total))