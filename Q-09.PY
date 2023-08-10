lista_de_compras = ["Arroz", "Feijão", "Macarrão", "Carne", "Frutas", "Verduras", "Pão", "Leite",
                    "Ovos", "Cereal", "Produtos de Limpeza", "Sorvete"]

sorvete_consumido = lista_de_compras.pop(-1)  

print("Lista de Compras do Mês (sem Sorvete):")
for item in lista_de_compras:
    print(item)

print("\nVocê se empanturrou de sorvete e removeu-o da lista.")
