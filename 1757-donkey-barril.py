'''
2
5 4
0 1
0 2
0 3
0 4
5 4
0 1
0 2
0 3
2 4

'''
import heapq
from collections import defaultdict


def Dijkstra(custo, total_vertices):
    distancia = [total_vertices] * total_vertices
    distancia[0] = 0

    fila = []
    heapq.heappush(fila, (0, 0))

    while fila:
        c, v = heapq.heappop(fila)
        if distancia[v] < c:
            continue

        for r in set(range(total_vertices)) - {v}:
            p = custo[r][v]

            if distancia[r] > distancia[v] + p:
                distancia[r] = distancia[v] + p
                heapq.heappush(fila, (distancia[r], r))

    return distancia

total_testes = int(input())

for _ in range(total_testes):
    total_cidades, caminhos_em_terra = input().split()
    total_cidades, caminhos_em_terra = int(total_cidades), int(caminhos_em_terra)

    grafo = defaultdict(lambda: [0]*total_cidades)

    for caminho_em_terra in range(caminhos_em_terra):
        A, B = input().split()
        A, B = int(A), int(B)

        grafo[A][B] = 1
        grafo[B][A] = 1

    print(max(Dijkstra(grafo, total_cidades)))
