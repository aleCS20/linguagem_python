# mercadoria com desconto e preço a pagar

valorMercadoria = float(input("Digite o valor da mercadoria: R$ "))
percentualDesconto = float(input("Digite o percentual de desconto: % "))

valorDesconto = valorMercadoria * (percentualDesconto/100)
valorComDesconto = valorMercadoria - valorDesconto

print(f"Valor do desconto: R$ {valorDesconto:.2f}")
print(f"Valor da mercadoria com desconto: R$ {valorComDesconto:.2f}")
