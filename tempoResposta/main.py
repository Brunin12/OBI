n_registros = int(input())

if not (1 <= n_registros <= 20):
    exit()

registros = []
tempo_total = 0
tempos_resposta = {}
mensagens_recebidas = {}

for _ in range(n_registros):
    entrada = input().split(' ')
    tipo = str(entrada[0])
    valor = int(entrada[1])

    if not (1 <= valor <= 100):
        exit()

    if tipo == 'R':
        mensagens_recebidas[valor] = tempo_total  # Armazena o tempo em que a mensagem foi recebida
    elif tipo == 'E':
        if valor in mensagens_recebidas:
            tempo_resposta = tempo_total - mensagens_recebidas[valor]
            if valor in tempos_resposta:
                tempos_resposta[valor] += tempo_resposta
            else:
                tempos_resposta[valor] = tempo_resposta
            del mensagens_recebidas[valor]  # Remove a mensagem recebida da lista
    elif tipo == 'T':
        tempo_total += valor - 1  # Adiciona o tempo extra, considerando que já há 1 segundo padrão entre eventos

    tempo_total += 1  # Cada evento conta 1 segundo

# Qualquer amigo com mensagens não respondidas recebe um tempo de resposta de -1
for amigo in mensagens_recebidas:
    tempos_resposta[amigo] = -1

# Ordena os amigos pelo número e prepara a saída
resultado = sorted(tempos_resposta.items())

for amigo, tempo in resultado:
    print(f"{amigo} {tempo}")
