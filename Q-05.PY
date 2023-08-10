idades = []
for i in range(20):
    idade = int(input(f"Digite a idade {i+1}: "))
    idades.append(idade)

while idades:
    del idades[-1]  

if not idades:
    print("A lista de idades está vazia.")
