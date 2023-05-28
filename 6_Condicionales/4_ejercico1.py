letra = input("ingresa letra ")
#if (letra=='a') or (letra=='e') or (letra=='i') or (letra=='o') or (letra=='u'):

if letra in 'aeiou':
    print("Es vocal")
else:
    print("no es vocal")