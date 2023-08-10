def sao_pares_inversos(palavra1, palavra2):
    return palavra1 == palavra2[::-1]

palavra1 = input("Digite a primeira palavra: ")
palavra2 = input("Digite a segunda palavra: ")

if sao_pares_inversos(palavra1, palavra2):
    print("As palavras são um par inverso.")
else:
    print("As palavras não são um par inverso.")
