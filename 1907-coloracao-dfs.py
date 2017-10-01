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


def dfs(l, c):
    matriz[l][c] = 'o'

    for i, j in direcoes:
        if 0 <= l+i < linhas \
        and 0 <= c + j < colunas:
            if matriz[l+i][c+j] == '.':
                dfs(l+i, c+j)


for i in range(linhas):
    matriz.append(list(input()))

resposta = 0

for i, linha in enumerate(matriz):
    for j, coluna in enumerate(linha):
        if coluna == '.':
            dfs(i, j)
            resposta += 1

print(resposta)
