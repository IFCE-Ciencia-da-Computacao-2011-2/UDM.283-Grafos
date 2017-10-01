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


def bfs(l, c):
    fila = [(l, c)]
    matriz[l][c] = 0

    while fila:
        l, c = fila.pop(0)

        for i, j in direcoes:
            if matriz[l+i][c+j] == '.':
                matriz[l+i][c+j] = 0
                fila.append((l+i, c+j))


matriz.append([None] * (colunas+2))
for i in range(linhas):
    matriz.append([None] + list(input()) + [None])
matriz.append([None] * (colunas+2))


resposta = 0


for i in range(1, linhas+1):
    for j in range(1, colunas+1):
        if matriz[i][j] == '.':
            bfs(i, j)
            resposta += 1

print(resposta)
