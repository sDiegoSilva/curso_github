# Este programa deve servir como caixa registradora.
# Cada produto na lista tem um código e o valor.
# O programa deve usar o código e a quantidade fornecidos pelo usuario
# e calcular o valor final.

codigo_produto = int(input("Digite o código do produto: "))
quantidade_produto = int(input("Digite a quantidade comprada: "))

if codigo_produto == 1:
    valor_pago = 5.0 * quantidade_produto
elif codigo_produto == 2:
    valor_pago = 3.5 * quantidade_produto
elif codigo_produto == 3:
    valor_pago = 4,80 * quantidade_produto
elif codigo_produto == 4:
    valor_pago = 8.90 * quantidade_produto
else:
    codigo_produto == 5
    valor_pago = 7.32 * quantidade_produto

print(f"Valor final da compra ficou em R${valor_pago:4.2f}.")
