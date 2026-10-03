#print(chr("A"))
print("ingresa una contraseña")

cont = input()
minus = 0
mayus = 0
numbr = 0
spec = 0
long = 0

for i in cont:
    #print(i)
    if ord(i) >= 97 and ord(i) <= 122:
        minus = 1
    if ord(i) >= 65 and ord(i) <= 90:
        mayus = 1
    if ord(i) >= 48 and ord(i) <= 57:
        numbr = 1
    if (ord(i) >= 33 and ord(i) <= 47) or (ord(i) >= 58 and ord(i) <= 64) or (ord(i) >= 91 and ord(i) <= 96) or (ord(i) >= 123 and ord(i) <= 126):
        spec = 1
if len(cont) >= 8:
    long = 1

if minus == 1 and mayus == 1 and numbr == 1 and spec == 1 and long == 1:
    print("la contraseña es segura")
else:
    print ("la contraseña NO es segura porque:")
    if minus == 0:
        print("la contraseña no tiene minusculas")
    if mayus == 0:
        print("la contraseña no tiene mayusculas")
    if numbr == 0:
            print("la contraseña no tiene numeros")
    if spec == 0:
            print("la contraseña no tiene caracteres especiales")
    if long == 0:
            print("la contraseña tiene menos de ocho caracteres")