# Este programa deve ler a quantidade de glicose no sangue de uma pessoa
# Apos a leitura de glicose, deve mostrar na tela a clssificação.
# REF:. Normal até 100mg/dl
# Elevado maior que 100 até 140mg/dl
# Diabetes maior de 140mg/dl

valor_glicose = float(input("Digite a medida da glicose: "))

if valor_glicose <= 100:
    print("Classificação: Normal")
elif valor_glicose <= 140:
    print ("Classificação: Elevado")
else:
    print("Classificação: Diabetes")
    print("Procure um médico!")