'''
4 5
1 2 1
1 3 2
2 4 1
3 4 1
4 1 2
3 2
1 2 2
1 3 2
3 2
1 2 2
1 3 1
4 2
1 2 2
3 4 2
0 0
'''
from collections import defaultdict

grafo = defaultdict(list)


N, M = input().split()
N, M = int(N), int(M)

V, W, P = input().split()
V, W, P = int(V), int(W), int(P)

grafo[V].append(W)
if P == 2:
    grafo[W].append(V)
