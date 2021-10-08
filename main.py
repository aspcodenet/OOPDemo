lista = [1,2,3,4,8,12]
nyaLista = []

oddIndex = True
for i in lista:
    if oddIndex == True:
        first = i
        oddIndex = False
    else:
        nyaLista.append(i)
        nyaLista.append(first)
        oddIndex = True

print(nyaLista)        


