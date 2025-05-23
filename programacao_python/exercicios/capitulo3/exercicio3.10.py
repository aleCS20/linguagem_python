# aumento salarial com percentual

salario = float(input("Digite o seu salário: R$ "))
percentual = float(input("Digite o percentual de aumento: % "))

aumento = salario * (percentual/100)
salarioFinal = salario + aumento
print(f"Valor do aumento: R$ {aumento:.2f}")
print(f"Valor do salário com aumento: R$ {salarioFinal:.2f}")