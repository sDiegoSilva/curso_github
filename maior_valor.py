# Este programa deve ser capaz de ler número e mostrar o maior entre eles

num1 = float(input("Escreva o primeiro número: "))
num2 = float(input("Escreva o segundo número: "))
num3 = float(input("Escreva o terceiro número: "))

if (num1 > num2) and (num1 > num3):
    maior_numero = num1
elif num2 > num3:
    maior_numero = num2
else:
    maior_numero = num3

print(f"Maior número entre os três é o {maior_numero:.2f}.")