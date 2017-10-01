from grafo import Grafo

from sys import stdin


def ler_grafo_input():
    return ler_grafo(stdin)


def ler_grafo_arquivo(path):
    with open(path) as file:
        return ler_grafo(file)


def ler_grafo(data):
    grafo = Grafo()

    for line in data:
        vertice1, vertice2 = line.strip().split()
        grafo.adicionar_aresta(vertice1, vertice2)

    return grafo

