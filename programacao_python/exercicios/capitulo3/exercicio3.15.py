# redução do tempo de vida de um fumante

quantidadeCigarros = int(input("Digite a quantidade de cigarros por dia: "))
anosFumando = int(input("Digite a quantidade de anos fumando: "))

minutosPerdidos = (quantidadeCigarros * 10) * (anosFumando * 365)
diasPerdidosTotal = minutosPerdidos / (24 * 60)

print(f"Redução do tempo de vida - dias: {diasPerdidosTotal:.2f}")
