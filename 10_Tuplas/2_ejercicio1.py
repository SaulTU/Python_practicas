meses = 'enero','febrero','marzo', 'abril','mayo','junio','julio', 
'agosto', 'septiembre','octubre','noviembre','diciembre'

a=int(input("Ingresa numero del mes "))
a-=1
if a in range(12):
    print(meses[a])
else:
    print("No corresponde a un mes")