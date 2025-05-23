# encontrar o valor a pagar por um carro alugado

kmPercorridos = float(input("Digite os quilometros percorridos: km "))
diasAlugados = int(input("Digite a quantidade de dias alugados: "))

precoTotal = (kmPercorridos * 0.15) + (diasAlugados * 60)
print(f"Valor total a pagar pelo aluguel do carro: R$ {precoTotal:.2f}")


