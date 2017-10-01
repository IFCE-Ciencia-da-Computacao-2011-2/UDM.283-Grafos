'''
2
3 4
1 0 1 1
1 0 0 1
0 1 1 0
1 1
5 3
1 0 0
0 1 0
0 1 1
0 1 1
1 0 0
2 2
'''

direcoes = [(0, -1), (0, 1), (1, 0), (-1, 0),
            (-1, -1), (-1, 1), (1, -1), (1, 1)]

A, B, matriz = None, None, None


def arvore_vizinhos(l, c):
    return [(l+i, c+j) for i, j in direcoes if 0 <= l + i < A and 0 <= c + j < B and matriz[l+i][c+j] == '1']


def vizinhos(l, c):
    return [(l+i, c+j) for i, j in direcoes if 0 <= l + i < A and 0 <= c + j < B]


def bfs(l, c):
    matriz[l][c] = -1
    fila = [[(l, c)]]

    turno = -1

    while fila:
        turno += 1
        novos_vizinhos = []

        for l, c in fila.pop(0):
            for i, j in arvore_vizinhos(l, c):
                matriz[i][j] = -1
                novos_vizinhos.append((i, j))

        if novos_vizinhos:
            fila.append(novos_vizinhos)

    return turno


total_testes = int(input())

for _ in range(total_testes):
    A, B = input().split()
    A, B = int(A), int(B)

    matriz = []
    for linha in range(A):
        matriz.append(input().split())

    l, c = input().split()
    l, c = int(l) - 1, int(c) - 1

    print(bfs(l, c))
