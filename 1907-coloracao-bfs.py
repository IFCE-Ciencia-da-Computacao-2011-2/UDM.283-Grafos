'''
6 9
.ooo.ooo.
o...o...o
.o.....o.
..o...o..
...o.o...
....o....
'''

linhas, colunas = input().split()
linhas, colunas = int(linhas), int(colunas)

matriz = []

direcoes = [(0, -1), (0, 1), (1, 0), (-1, 0)]


def vizinhos(l, c):
    return [(l+i, c+j) for i, j in direcoes if 0 <= l + i < linhas and 0 <= c + j < colunas]


def bfs(l, c):
    fila = [(l, c)]
    matriz[l][c] = 0

    while fila:
        l, c = fila.pop(0)

        for i, j in vizinhos(l, c):
            if matriz[i][j] == '.':
                matriz[i][j] = 0
                fila.append((i, j))


for i in range(linhas):
    matriz.append(list(input()))

resposta = 0

for i, linha in enumerate(matriz):
    for j, coluna in enumerate(linha):
        if coluna == '.':
            bfs(i, j)
            resposta += 1

print(resposta)
