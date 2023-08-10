lista_de_compras = ["Arroz", "Feijão", "Macarrão", "Carne", "Frutas", "Verduras", "Pão", "Leite",
                    "Ovos", "Cereal", "Produtos de Limpeza", "Sorvete"]

lista_de_compras.remove("Produtos de Limpeza")

print("Lista de Compras do Mês (sem Produtos de Limpeza):")
for item in lista_de_compras:
    print(item)
