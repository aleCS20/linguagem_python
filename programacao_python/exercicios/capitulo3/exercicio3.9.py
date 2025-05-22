# dias - horas - minutos - segundos ---> calcular o total em segundos

dias = int(input("Digite os dias: "))
horas = int(input("Digite as horas: "))
minutos = int(input("Digite os minutos: "))
segundos = int(input("Digite os segundos: "))

total_segundos = (dias * 24 * 3600) + (horas * 3600) + (minutos * 60 + segundos)
print(f"O total convertido em segundos e: {total_segundos}")