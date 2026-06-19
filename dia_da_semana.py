# Programa que diz qual o dia da semana de acordo com o número digitado
numero_dia_semana = int(input("Digite um número de 1 a 7 para saber qual é o dia da semana: "))
if numero_dia_semana == 1:
    print("O dia da semana é: Domingo")
elif numero_dia_semana == 2:
    print("O dia da semana é: Segunda-feira")
elif numero_dia_semana == 3:
    print("O dia da semana é: Terça-feira")
elif numero_dia_semana == 4:
    print("O dia da semana é: Quarta-feira")
elif numero_dia_semana == 5:
    print("O dia da semana é: Quinta-feira")
elif numero_dia_semana == 6:
    print("O dia da semana é: Sexta-feira")
elif numero_dia_semana == 7:
    print("O dia da semana é: Sábado")
else:
    print("Número inválido. Por favor, digite um número de 1 a 7.")