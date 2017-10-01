"""
Resultado = (Total de arestas - 1) * 2
"""
total_testes = int(input())
for _ in range(total_testes):
    input()
    total = input().split()
    vertices_participantes = set()

    for i in range(int(total[1])):
        origem, destino = input().split()
        vertices_participantes |= {int(origem), int(destino)}

    print((len(vertices_participantes)-1)*2)
