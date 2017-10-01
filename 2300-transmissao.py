def dfs(no, grafo, visitados):
    if no in visitados:
        return visitados

    visitados |= {no}
    for destino in grafo[no]:
        dfs(destino, grafo, visitados)

    return visitados


line = ''
indice = 0
while True:
    indice += 1
    grafo = dict()

    linha = input()
    if linha == '0 0':
        break

    total_vertices, total_arestas = linha.split()
    total_vertices = int(total_vertices)
    total_arestas = int(total_arestas)

    for j in range(total_vertices):
        grafo[j + 1] = []

    for i in range(total_arestas):
        origem, destino = input().split()
        origem = int(origem)
        destino = int(destino)

        grafo[origem].append(destino)
        grafo[destino].append(origem)

    print('Teste {}'.format(indice))

    #no = next(iter(grafo))
    no = list(grafo.keys())[0]
    visitados = dfs(no, grafo, set())
    print('normal' if len(visitados) == total_vertices else 'falha')

    print()
