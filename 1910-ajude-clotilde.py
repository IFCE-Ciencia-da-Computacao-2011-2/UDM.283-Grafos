'''
3 8 2
4 5
2 5 5
1 3 10 6 4
13 1 4
15 12 100 5
0 0 0
'''

operacoes = [lambda e: e-1, lambda e: e+1, lambda e: int(e/2) if e % 2 == 0 else -1, lambda e: e*2, lambda e: e*3]

MAX_D = 10**5


def entrada():
    origem, destino, K = input().split()
    origem, destino, K = int(origem), int(destino), int(K)

    proibidos = [int(e) for e in input().split()] if K > 0 else []

    return origem, destino, proibidos


def analizar(origem, destino, proibidos):
    total_movimentos = 0
    a_visitar = [origem]

    #visitados = set(proibidos)
    visitados = [False] * (MAX_D+1)
    for proibido in proibidos:
        visitados[proibido] = True

    while a_visitar:
        proximos_a_visitar = []
        total_movimentos += 1

        for elemento in a_visitar:
            for operacao in operacoes:
                resultado = operacao(elemento)

                #if resultado in visitados \
                if not (0 < resultado <= MAX_D) \
                or visitados[resultado]:
                    continue
                elif resultado == destino:
                    return total_movimentos

                #visitados |= {resultado}
                visitados[resultado] = True
                proximos_a_visitar.append(resultado)

        a_visitar = proximos_a_visitar

    return -1


while True:
    origem, destino, proibidos = entrada()

    if origem == 0 and destino == 0:
        break

    print(analizar(origem, destino, proibidos))
