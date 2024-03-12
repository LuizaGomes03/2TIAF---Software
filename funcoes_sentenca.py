def encontrar_verbo(frase):
    """
    Esta função encontra o verbo principal de uma frase.

    Args:
        frase (str): A frase a ser analisada.

    Returns:
        str: O verbo principal da frase, ou None se não for encontrado.
    """
    
    # Dividir a frase em palavras
    palavras = frase.lower().split()

    # Verbos auxiliares
    verbos_auxiliares = ["ser", "estar", "ter", "haver", "poder", "dever", "saber", "ir", "fazer"]

    # Converter verbos de ligação em lista
    verbos_ligacao = ["ser", "estar", "parecer"]

    for i, palavra in enumerate(palavras):
        # Se a palavra for um verbo no infinitivo
        if palavra.endswith(("ar", "er", "ir")) or (palavra == "ser" and i > 0):
            # Se a palavra não for um verbo auxiliar ou de ligação
            if palavra not in verbos_auxiliares + verbos_ligacao:
                return palavra

    # Se nenhum verbo foi encontrado
    return None

# Mensagem para o usuário
frase_usuario = input("Digite a frase: ")

# Chamar a função e mostrar o resultado
verbo_encontrado = encontrar_verbo(frase_usuario)
if verbo_encontrado:
    print(f"O verbo principal na frase '{frase_usuario}' é: {verbo_encontrado}")
else:
    print("Nenhum verbo principal foi encontrado na frase.")
