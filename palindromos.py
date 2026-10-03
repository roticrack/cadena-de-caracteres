print("ingresa una palabra")
palab = input()
palind = 1
times = 0
oppos = len(palab) - 1

for i in palab:
    if i != palab[oppos]:
        palind = 0
    times += 1
    oppos -= 1

if palind == 1:
    print("la palabra es un palindromo")
else:
    print("la palabra NO es un palindromo")