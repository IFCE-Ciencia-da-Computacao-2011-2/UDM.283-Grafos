from collections import defaultdict
from utils import vertices_conexos_a_partir_de


class Grafo(object):
    def __init__(self):
        self._grafo = defaultdict(set)
        self.total_arestas = 0

    @property
    def vertices(self):
        return list(self._grafo.keys())

    def remover_aresta(self, vertice1, vertice2):
        if not self.has_aresta(vertice1, vertice2):
            raise Exception("Aresta ({}, {}) não pertence ao grafo".format(vertice1, vertice2))

        self.total_arestas -= 1

        self._grafo[vertice1] -= {vertice2}
        self._grafo[vertice2] -= {vertice1}

    def adicionar_aresta(self, vertice1, vertice2):
        self.total_arestas += 1

        self._grafo[vertice1] |= {vertice2}
        self._grafo[vertice2] |= {vertice1}

    def __iter__(self):
        return self._grafo.__iter__()

    def __getitem__(self, vertice):
        return self._grafo[vertice]

    def is_conexo(self):
        return self.is_vertices_conexos(self.vertices)

    def is_vertices_conexos(self, vertices):
        vertice_inicial = list(vertices)[0]
        nos_visitados = vertices_conexos_a_partir_de(vertice_inicial, self)

        return nos_visitados == set(vertices)

    def is_ponte(self, vertice1, vertice2):
        if not self.has_aresta(vertice1, vertice2):
            raise Exception("Aresta ({}, {}) não pertence ao grafo".format(vertice1, vertice2))

        # Não considerar os vértices que não possuem arestas
        # vertices = {v: v ∈ V(G), |deg(v)| > 0}
        vertices = {vertice for vertice in self.vertices if self.grau(vertice) > 0}

        self.remover_aresta(vertice1, vertice2)
        conexo = self.is_vertices_conexos(vertices)
        self.adicionar_aresta(vertice1, vertice2)

        return not conexo

    def has_aresta(self, vertice1, vertice2):
        return vertice2 in self[vertice1]

    def grau(self, vertice):
        return len(self[vertice])

    def __str__(self):
        return self._grafo.__str__()
