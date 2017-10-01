'''
4
3
2
1 3
2 3
4
2
1 2
3 4
3
0
6
5
1 2
1 3
1 4
2 3
3 4

'''
from collections import defaultdict


def grupos(numero_pontos, grafo):
    total = set(range(1, numero_pontos + 1))
    visitados = set()
    total_grupos = 0

    while total != visitados:
        nao_visitados = total - visitados
        elemento = next(nao_visitados.__iter__())
        visitados |= dfs(elemento, grafo, set())
        total_grupos += 1

    return total_grupos


def dfs(no, grafo, visitados):
    if no in visitados:
        return visitados

    visitados |= {no}
    for destino in grafo[no]:
        visitados = dfs(destino, grafo, visitados)

    return visitados

total_testes = int(input())

for caso in range(total_testes):
    numero_pontos = int(input())
    numero_estradas = int(input())

    grafo = defaultdict(list)
    for _ in range(numero_estradas):
        A, B = input().split()
        A, B = int(A), int(B)

        grafo[A].append(B)
        grafo[B].append(A)

    falta = grupos(numero_pontos, grafo) - 1
    mensagem = 'a promessa foi cumprida' if falta == 0 else 'ainda falta(m) {} estrada(s)'.format(falta)

    print('Caso #{}: {}'.format(caso+1, mensagem))
