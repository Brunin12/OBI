# BRIEFING

# 3 grupos
# participantes que venceram 5 ou 6 jogos serão colocados no Grupo 1;
# participantes que venceram 3 ou 4 jogos serão colocados no Grupo 2;
# participantes que venceram 1 ou 2 jogos serão colocados no Grupo 3;
# participantes que não venceram nenhum jogo não serão convidados a continuar com os treinamentos.

# =====================================================================================================================

vitorias = 0

for i in range(6):
    resultadoPartida = str(input())

    if resultadoPartida == 'V':
        vitorias += 1

if vitorias in (1, 2):
    print(3)
elif vitorias in (3, 4):
    print(2)
elif vitorias in (5, 6):
    print(1)
else:
    print(-1)






