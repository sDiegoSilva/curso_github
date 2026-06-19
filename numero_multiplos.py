# Este programa deve ler dois números inteiros e 
# dizer se um número é múltiplo do outro.
# Os número podem ser digitados em qualquer ordem.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if (num1 % num2 == 0) or (num2 % num1 == 0):
    print("São multiplos.")
else:
    print("Não são multiplos.")