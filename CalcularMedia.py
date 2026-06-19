# ==========================================
# ARTEFATO 2: gerenciador_notas.py
# ==========================================
# -*- coding: utf-8 -*-

def calcular_media(notas):
    """
    Calcula a media aritmetica de uma lista de notas academicas.

    Esta funcao soma todas as notas fornecidas e realiza a divisao pelo 
    total de elementos na lista. Possui uma barreira de seguranca para 
    evitar erros de divisao por zero caso o estudante nao possua notas.

    Args:
        notas (list): Lista contendo valores flutuantes (floats) que 
                      representam as notas obtidas pelo estudante.

    Returns:
        float: O valor resultante da media aritmetica das notas. 
               Retorna 0.0 se a lista de entrada estiver vazia.
    """
    if len(notas) == 0:
        return 0.0
        
    soma_total = sum(notas)
    media_resultante = soma_total / len(notas)
    
    return media_resultante


def verificar_aprovacao(media, media_minima=7.0):
    """
    Avalia o status final do estudante com base na media obtida.

    Compara a media do estudante com a nota de corte parametrizada para 
    a instituicao de ensino, definindo de forma exata a situacao academica.

    Args:
        media (float): O valor da media final obtida pelo estudante.
        media_minima (float, opcional): A nota minima exigida para a 
                                        aprovacao. O valor padrao e 7.0.

    Returns:
        str: Retorna 'Aprovado' caso a media seja maior ou igual a 
             media_minima, ou 'Reprovado' caso seja inferior.
    """
    if media >= media_minima:
        return "Aprovado"
    else:
        return "Reprovado"


def gerar_relatorio(alunos):
    """
    Percorre a lista de dicionarios de alunos, calcula as medias,
    verifica as situacoes e exibe um relatorio organizado no terminal.
    
    Args:
        alunos (list): Lista contendo os dicionarios dos estudantes.
    """
    print("\n==================================================")
    print("      RELATÓRIO DE DESEMPENHO ACADÊMICO           ")
    print("==================================================")
    
    # O laco percorre cada dicionario dentro da lista principal de alunos
    for estudante in alunos:
        
        # Extrai os atributos essenciais definidos na estrutura de dados
        nome_aluno = estudante["nome"]
        notas_aluno = estudante["notas"]
        
        # Reaproveita as lógicas matemáticas isoladas (SRP)
        media_final = calcular_media(notas_aluno)
        situacao_final = verificar_aprovacao(media_final)
        
        # Exibe os dados de forma alinhada e nítida no terminal
        print(f"Estudante: {nome_aluno:15} | Média: {media_final:.1f} | Situação: {situacao_final}")
        
    print("==================================================\n")


# Bloco de execucao principal do sistema
if __name__ == "__main__":
    
    # Requisito: Lista de dicionarios com atributos "nome" e "notas"
    banco_estudantes = [
        {"nome": "Ana Silva", "notas": [8.5, 9.0, 7.5]},
        {"nome": "Bruno Souza", "notas": [5.0, 6.0, 4.5]},
        {"nome": "Carlos Lima", "notas": [7.0, 3.5, 6.0]}
    ]
    
    # Geracao do relatorio integrado
    gerar_relatorio(banco_estudantes)