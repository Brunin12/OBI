def cifrar_palavra(palavra):
    if len(palavra) < 1 or len(palavra) > 30:
        exit()

    # Definindo as vogais e o alfabeto
    vogais = "aeiou"
    alfabeto = "abcdefghijklmnopqrstuvwxyz"

    # Função auxiliar para encontrar a vogal mais próxima
    def vogal_mais_proxima(c):
        distancias = {v: abs(alfabeto.index(c) - alfabeto.index(v)) for v in vogais}
        return min(distancias, key=lambda k: (distancias[k], k))

    # Função auxiliar para encontrar a próxima consoante
    def proxima_consoante(c):
        pos = alfabeto.index(c)
        for i in range(pos + 1, len(alfabeto)):
            if alfabeto[i] not in vogais:
                return alfabeto[i]
        return c  # Se for 'z', retorna 'z'

    resultado = []
    for letra in palavra:
        if letra in vogais:
            resultado.append(letra)
        else:
            consoante = letra
            vogal = vogal_mais_proxima(letra)
            prox_consoante = proxima_consoante(letra)
            resultado.extend([consoante, vogal, prox_consoante])

    return ''.join(resultado)


print(cifrar_palavra(str(input())))
