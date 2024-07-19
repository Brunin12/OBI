# Lê o tamanho da sequência da entrada padrão
tamanho_seq = int(input())

# Verifica se o tamanho da sequência está fora dos limites permitidos
# Se o tamanho for menor que 3 ou maior que 500, o programa termina
if 3 > tamanho_seq or tamanho_seq > 500:
    exit()

# Inicializa uma lista vazia para armazenar a sequência de números
sequencia = []

# Loop para ler cada número da sequência
for i in range(tamanho_seq):
    # Lê um número da entrada padrão
    entrada = int(input())

    # Verifica se o número lido é válido (deve ser 1 ou 2)
    # Se o número não for 1 nem 2, o programa termina
    if entrada not in [1, 2]:
        exit()

    # Adiciona o número válido à sequência
    sequencia.append(entrada)


# Implementação da lógica de programação dinâmica para resolver o problema
def max_marked_sequence(n, sequence):
    # Array dp para armazenar o máximo de números marcados até cada posição
    dp = [0] * n

    # O primeiro número sempre pode ser marcado
    dp[0] = 1

    # Itera sobre a sequência para preencher o array dp
    for i in range(1, n):
        if sequence[i] != sequence[i - 1]:
            # Se o número atual é diferente do anterior, podemos marcá-lo
            dp[i] = dp[i - 1] + 1
        else:
            # Se o número atual é igual ao anterior, não podemos marcá-lo
            # Verificamos a melhor opção entre não marcá-lo ou pular um número
            if i > 1:
                dp[i] = max(dp[i - 1], dp[i - 2] + 1)
            else:
                dp[i] = dp[i - 1]

    # O resultado final é o máximo de números marcados até a última posição
    return dp[-1] - 1


# Chama a função para calcular o resultado e imprime
resultado = max_marked_sequence(tamanho_seq, sequencia)
print(resultado)
