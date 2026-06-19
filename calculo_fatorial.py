import math

# Solicita ao usuário um número e realiza a conversão explícita (casting) de string para inteiro (int).
# Esta conversão é necessária pois o cálculo de fatorial exige números inteiros.
numero_inteiro = int(input('Digite um número inteiro entre 1 e 10:  '))

# Utiliza o método factorial da biblioteca nativa math para realizar o processamento matemático.
fatorial_calculado = math.factorial(numero_inteiro)

# Exibe o resultado final utilizando f-string para apresentar o número original e o valor processado.
print(f"O fatorial de {numero_inteiro} é: {fatorial_calculado}")