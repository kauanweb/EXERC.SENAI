
numeros = []
for i in range(5):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(numero)

for i, numero in enumerate(numeros):
    print(f"O número {numero} está na posição {i+1} da lista.")
