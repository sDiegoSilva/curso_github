# Programa que calcula o valor a mais que deve ser pago a operadora por cada minuto
# Cada minuto que exceder, deve ser cobrado R$2,00 a mais no valor final.

print("Cálculo de valor da operadora. Assinatura de 100 minutos é R$50,00.")
minutos = int(input('Digite o tempo de ligação feito na semama: '))
VALOR_ASSINATURA = float(50)

if minutos <= 100:
    print(f"O valor da assinatura é R${VALOR_ASSINATURA}.")
else: 
    minutos > 100
    valor_assinatura = VALOR_ASSINATURA + 2 * (minutos - 100)
    print(f"O valor da assinatura é R${valor_assinatura:4.2f}.")
