def valor():
    a=float(input("Total"))
    b=int(input("Dame un 1 para aplicar IVA: "))
    if b==1:
        a=a*1.16
    else:
        a=a*1.21
    return a
print(valor())