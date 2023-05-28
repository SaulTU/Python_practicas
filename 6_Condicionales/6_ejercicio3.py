from os import remove

cad1="remo"
cad2="memo"
cad3="como"
cad4="sape"

if cad1[-2:] == cad4[-2:]:
    if cad1[-3:] == cad4[-3:]:
        print("rima")
    else:
        print("rima mas o menos")
else:
    print("no rima")