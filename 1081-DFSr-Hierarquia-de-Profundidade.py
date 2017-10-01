'''
2
12 9
0 1
1 5
5 6
0 4
4 2
2 3
7 8
1 7
10 11
11 8
0 1
1 2
3 4
4 3
5 6
6 8
7 9
9 10

'''
from collections import defaultdict


def ler_grafo():
    elementos_em_aresta = set()

    V, A = input().split()
    V, A = int(V), int(A)

    grafo = defaultdict(list)
    for _ in range(A):
        a, b = input().split()
        a, b = int(a), int(b)

        grafo[a].append(b)
        elementos_em_aresta |= {a, b}

    return grafo, V, A, elementos_em_aresta


def pathR(visitados, e, contexto=2):
    visitados |= {e}

    for n in grafo[e]:
        if n not in visitados:
            print('{}{}-{} pathR(G,{})'.format(' '*contexto, e, n, n))
            pathR(visitados, n, contexto+2)
        else:
            print('{}{}-{}'.format(' '*contexto, e, n))


total_testes = int(input())

for caso in range(total_testes):
    grafo, V, A, elementos_em_aresta = ler_grafo()

    print('Caso {}:'.format(caso + 1))

    visitados = set()

    for e in elementos_em_aresta:
        if e in visitados:
            continue

        pathR(visitados, e)
        print()
