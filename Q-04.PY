idades = []
for i in range(20):
    idade = int(input(f"Digite a idade {i+1}: "))
    idades.append(idade)

maior_idade = max(idades)
menor_idade = min(idades)

print(f"Maior idade: {maior_idade}")
print(f"Menor idade: {menor_idade}")
