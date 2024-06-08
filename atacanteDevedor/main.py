# Criar variáveis
num_amigos = int(input())
quantidade_emprestada = []
quantidade_presa = []
resultado_recebeu = 0
resultado_pagou = 0
recebeu = []
pagou = []

# Definir variáveis
quantidade_emprestada = [int(num) for num in input().split()]
quantidade_presa = [int(num) for num in input().split()]

# Fazer saída

# Fazer um loop usando os dois arrays juntos dentro dele e guardar o produto da subtração de um com outro
for i in range(num_amigos):
    emprestado_temp = quantidade_emprestada[i]
    preso_temp = quantidade_presa[i]

    if emprestado_temp > preso_temp:
        recebeu.append(emprestado_temp - preso_temp)
    else:
        pagou.append(preso_temp - emprestado_temp)

for i in recebeu:
    resultado_recebeu += i

for i in pagou:
    resultado_pagou += i

print(resultado_recebeu, resultado_pagou)
