megalonomeslista = []
nome = ""
for i in range (5):
    nome = input("bota: ")
    megalonomeslista.append(nome.capitalize())

megalonomeslista.sort()
print(megalonomeslista)