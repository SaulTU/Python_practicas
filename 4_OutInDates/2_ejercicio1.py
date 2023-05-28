a = int(input("ingresa a: "))
b = int(input("ingresa b: "))
c = int(input("ingresa c: "))
r= pow(b,2)-(4*a*c)
x1 = (-b + pow(r,1/2))/(2*a)
x2 = (-b - pow(r,1/2))/(2*a)

print("Solucion",x1)
print("Solucion",x2)