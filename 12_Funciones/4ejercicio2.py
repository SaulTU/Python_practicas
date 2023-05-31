def factorial(num):
    a=1
    i=1
    while i<=num:
        a=i*a
        i+=1
    print(a)

a = int(input('FActorial num: '))
factorial(a)