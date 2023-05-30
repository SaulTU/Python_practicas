from ctypes import sizeof


meses = ('a','b','c', 'd','e','f','g', 'h', 'i','j','k','l', 'm', 'n',
'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

a=int(input("Ingresa numero de letra "))
a-=1
if a in range(meses.__sizeof__()):
    print(meses[a])
else:
    print("No corresponde a un mes")