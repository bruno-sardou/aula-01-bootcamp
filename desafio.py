nome = input("Digite seu nome: ")
salario = float(input("Digite seu salário: "))
valor_bonus = float(input("Digite o valor do bônus: "))
percentual_bonus = valor_bonus / salario * 100

print(f'Parabéns, {nome}. O bônus recebido corresponde à {percentual_bonus:.2f}% do seu salário.')