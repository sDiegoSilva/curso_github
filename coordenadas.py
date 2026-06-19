# Este programa ler as coordenadas de X e Y no plano cartesiano e
# determinar qual o quadrante pertence o ponto. Se o ponto estiver
# na origem, deve escrever "Origem". Se estiver sobre um dos eixos, 
# escreva "Eixo X" ou "Eixo Y".
#   Q2 | Q1
# X----|-----
#   Q3 | Q4
#      Y

valor_x = float(input("Digite o valor de X: ")) 
valor_y = float(input("Digite o valor de Y: "))

if valor_x > 0 and valor_y > 0:
    print("Q1")
elif valor_x < 0 and valor_y > 0:
    print("Q2")
elif valor_x < 0 and valor_y < 0:
    print("Q3")
elif valor_x > 0 and valor_y < 0:
    print("Q4")
elif valor_x == 0 and valor_y == 0:
    print("Origem")
elif valor_x == 0:
    print("Eixo Y")
else:
    valor_y == 0
    print("Eixo X")

