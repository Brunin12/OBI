tamanho_album = int(input())
if 1 > tamanho_album or tamanho_album > 100:
    exit()

fig_compradas = int(input())
if 1 > fig_compradas or fig_compradas > 300:
    exit()

album = []
for i in range(fig_compradas):
    entrada = int(input())
    if 1 > entrada or entrada > tamanho_album:
        exit()

    if entrada not in album:
        album.append(entrada)

print(tamanho_album - len(album))