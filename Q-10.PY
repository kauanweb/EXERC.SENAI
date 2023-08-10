def verificar_par_impar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

numero_teste = int(input("Digite um número: "))
resultado = verificar_par_impar(numero_teste)
print(f"O número {numero_teste} é {resultado}.")
