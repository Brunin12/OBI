# FUNÇÕES

def entradaIdade():
    idade = int(input())

    if 5 > idade or idade > 100:
        exit()

    return idade


def gerarMediana(idades):
    tamanho = len(idades)
    idades.sort()

    if tamanho % 2 == 0:
        mediana1 = idades[tamanho // 2]
        mediana2 = idades[tamanho // 2 - 1]

        return (mediana1 + mediana2) / 2
    else:
        return idades[tamanho // 2]


# COLETA E VERIFICAÇÃO DOS DADOS DE ENTRADA

idades = []

idades.append(entradaIdade())

idades.append(entradaIdade())

idades.append(entradaIdade())

# SAIDA

resultado = gerarMediana(idades)

print(resultado)
