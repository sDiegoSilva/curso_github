# Este programa deve calcular aumento salarial dentro de uma empresa.
# TABELA PARA REFERENCIA
# Salário até R$1000 recebe 20% de aumento
# Salário acima de R$1000 até R$3000 recebe 15% de aumento
# Salário acima de R$3000 até R$8000 recebe 10% de aumento
# Salário acima de R$8000 recebe 5% de aumento

salario_atual = float(input("Digite o salário atual da pessoa: "))
print(salario_atual)

if salario_atual <= 1000:
    porcentagem = 20
elif salario_atual <= 3000:
    porcentagem = 15
elif salario_atual <= 8000:
    porcentagem = 10
else:
    porcentagem = 5

aumento = salario_atual * porcentagem / 100
novo_salario = salario_atual + aumento

print(f"Você recebeu {porcentagem}% de aumento. Isso equivale a R${aumento:5.2f} de aumento.")
print(f"Seu salário novo salário é R${novo_salario:5.2f}.")