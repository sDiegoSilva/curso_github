# Este programa de fazer a conversão de temperatura
# O usuario pode escolher se quer converter Fahrenheit para Celsius ou vice-versa

escala_temperatura = str(input("Escolha a escala de temperatura para converter: (C/F)"))

if escala_temperatura == "F":
    fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)
    print(f"Temperatura equivalente em Celsius: {celsius:4.2f}°C")
elif escala_temperatura == "C":
    celsius = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = 9 * celsius / 5 + 32
    print(f"Temperatura equivalente em Fahrenheit: {fahrenheit:4.2f}°F")
else:
    print("Entrada inválida! Escolha entre C ou F.")