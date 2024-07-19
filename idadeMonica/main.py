idadeMonica = int(input())
filhos = []
if 40 > idadeMonica or idadeMonica > 110:
    exit()

filhos.append(int(input()))
if 1 > filhos[0] or filhos[0] > idadeMonica:
    exit()

filhos.append(int(input()))
if 1 > filhos[1] or filhos[1] > idadeMonica or filhos[0] == filhos[1]:
    exit()

filhos.append(idadeMonica - (filhos[0] + filhos[1]))

print(max(filhos))