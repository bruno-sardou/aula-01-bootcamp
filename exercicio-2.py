valor_1 = input("Digite o primeiro valor: ")
valor_2 = input("Digite o segundo valor: ")

if valor_1.isnumeric() and valor_2.isnumeric():
    print(f'A soma dos valores é {int(valor_1) + int(valor_2)}.')