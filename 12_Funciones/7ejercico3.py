def valor():
    a=int(input("Dame un numero: "))
    b=int(input("Dame un numero: "))
    if a==b:
        c=0
    elif a>b:
        c=1
    else:
        c=-1
    return c
print(valor())