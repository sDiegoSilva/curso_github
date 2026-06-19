# JOGO DA FORCA 

import random

def inicializar_jogo():
    """
    Função responsável por preparar o jogo.
    Sorteia a palavra e cria as estruturas de dados iniciais.
    Retorna a palavra, a lista de lacunas, o conjunto de tentativas e as vidas.
    """
    # 1. Lista de palavras disponíveis (Vocabulário)
    lista_palavras = ["PYTHON", "ALGORITMO", "ESTRUTURA", "COMPUTADOR", "INTERFACE", "DESENVOLVEDOR", "PROGRAMAÇÃO", "SOFTWARE", "HARDWARE", "DADOS", "VARIÁVEL", "FUNÇÃO", "CLASSE", "OBJETO", "HERANÇA", "ENCAPSULAMENTO", "ABSTRAÇÃO", "ALGORITMO", "LÓGICA", "DEPURAÇÃO", "TESTE", "GITHUB", "REPOSITÓRIO", "FRAMEWORK", "BIBLIOTECA", "SCRIPT", "AUTOMAÇÃO", "INTELIGÊNCIA", "ARTIFICIAL", "MACHINE", "LEARNING", "NEURAL", "NETWORKS"]
    
    # 2. Sorteio aleatório da palavra
    palavra_secreta = random.choice(lista_palavras)
    
    # 3. Cria a lista com os espaços vazios (['_', '_', '_'])
    # Multiplicamos o caractere pelo tamanho da palavra
    palavra_mascarada = ["_"] * len(palavra_secreta)
    
    """
    CONJUNTO (SET):
    Optei por usar um (set) em vez de uma lista porque
    conjuntos matemáticos não aceitam elementos repetidos. Se o jogador 
    digitar a letra 'A' duas vezes, o set ignora a repetição automaticamente.
    """

    letras_tentadas = set()
    
    # 4. Define o limite de erros
    tentativas_restantes = 6
    
    return palavra_secreta, palavra_mascarada, letras_tentadas, tentativas_restantes


def processar_tentativa(letra_digitada, palavra_secreta, palavra_mascarada):
    """
    Verifica se a letra digitada está dentro da palavra secreta.
    Se estiver, atualiza a lista de lacunas na posição correta.
    Retorna True se o jogador acertou a letra, e False se errou.
    """
    acertou = False
    
    # Usamos range(len()) para percorrer cada posição (índice) da palavra secreta
    # É a forma clássica de verificar letra por letra em lógica de programação
    for posicao in range(len(palavra_secreta)):
        
        if palavra_secreta[posicao] == letra_digitada:
            # Se achou a letra, troca o '_' pela letra na mesma posição
            palavra_mascarada[posicao] = letra_digitada
            acertou = True
            
    return acertou


def jogar_forca():
    """
    Função principal que coordena o laço de repetição e as interações com o usuário.
    """
    # Recebendo os dados iniciais
    palavra_secreta, palavra_mascarada, letras_tentadas, tentativas_restantes = inicializar_jogo()
    
    print("Bem-vindo ao Jogo da Forca!")
    print("Tente adivinhar a palavra secreta.")
    
    # LAÇO PRINCIPAL: roda enquanto houverem tentativas E a palavra tiver '_' (lacunas)
    while tentativas_restantes > 0 and "_" in palavra_mascarada:
        
        # Mostra as informações para o jogador
        print("\n--- STATUS DO JOGO ---")
        print("Palavra atual:", " ".join(palavra_mascarada))
        print("Tentativas restantes:", tentativas_restantes)
        
        # Mostra o conjunto de letras já tentadas (convertido para lista para ordenar)
        print("Letras já tentadas:", sorted(list(letras_tentadas)))
        print("----------------------")
        
        # Coleta a letra e transforma em maiúscula para não dar erro
        palpite = input("Digite uma letra: ").upper()
        
        # Validação básica: garante que o usuário digitou só 1 caractere
        if len(palpite) != 1:
            print("Aviso: Digite apenas uma única letra por vez!")
            continue
            
        # Validação básica: verifica se a letra já está no nosso conjunto (set)
        if palpite in letras_tentadas:
            print("Aviso: Você já tentou essa letra. Tente uma nova!")
            continue
            
        # Guarda a letra nova no histórico
        letras_tentadas.add(palpite)
        
        # Envia a letra para ser processada pela nossa outra função
        se_acertou = processar_tentativa(palpite, palavra_secreta, palavra_mascarada)
        
        # Exibe o resultado da rodada
        if se_acertou == True:
            print("Muito bem! Você acertou a letra.")
        else:
            print("Que pena! Essa letra não existe na palavra.")
            tentativas_restantes = tentativas_restantes - 1
            
    # Verifica como o laço while terminou (Vitória ou Derrota)
    print("\n--- RESULTADO FINAL ---")
    if "_" not in palavra_mascarada:
        print("Parabéns! Você adivinhou a palavra:", palavra_secreta)
    else:
        print("Suas tentativas acabaram! A palavra era:", palavra_secreta)


# Inicia a execução do programa chamando a função principal
jogar_forca()