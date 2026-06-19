# Programa para verificar se tem mais ou menos que 90 dias de garantia apos sair da assistencia tecnica

tempo_restante_garantia = int(input("Digite o tempo restante da garantia em dias: "))
soma_garantia = 90 - tempo_restante_garantia

if tempo_restante_garantia >= 90:
    print(f"Sua garantia ainda está ativa por mais {tempo_restante_garantia} dias.")
else:
    tempo_restante_garantia < 90
    print(f"Acrecentamos mais {soma_garantia} dias à sua garantia, para que você não tenha menos que 90 dias.")


