# Este programa deve calcular o tempo de jogo.
# O programa recebe a hora inicial e final de um jogo e vai calcular a duração.
# Cada jogo tem a duração mínima de 1 hora e máxima de 24 horas.
# Os jogos podem começar em um dia e terminar no outro.

hora_inicial = int(input("Digite a hora inicial do jogo: ")) 
hora_final = int(input("Digite a hora final do jogo: "))

if hora_inicial < hora_final:
    duracao = hora_final - hora_inicial
else:
    duracao = 24 - hora_inicial + hora_final

print(f"O jogo durou {duracao} horas.")