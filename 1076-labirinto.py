'''
2
0
16 15
0 4
2 3
6 2
8 9
10 9
8 12
14 15
14 10
6 5
10 11
11 7
4 8
0 1
1 2
12 13
1
9 6
1 2
1 4
4 7
7 8
4 1
4 3
'''
def dfs(no, grafo, visitados, contador):
    if no in visitados:
        return contador + 1

    visitados |= {no}
    for destino in grafo[no]:
        contador = dfs(destino, grafo, visitados, contador)

    return contador + 1


total_testes = int(input())

for _ in range(total_testes):
    posicao_inicial = int(input())
    grafo = dict()

    total_vertices, total_arestas = input().split()
    total_vertices = int(total_vertices)
    total_arestas = int(total_arestas)

    for j in range(total_vertices):
        grafo[j] = set()

    for i in range(total_arestas):
        origem, destino = input().split()
        origem = int(origem)
        destino = int(destino)

        grafo[origem].add(destino)
        grafo[destino].add(origem)

    print(dfs(posicao_inicial, grafo, set(), 0) - 1)
