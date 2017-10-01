from ler_entrada import ler_grafo_input, ler_grafo_arquivo


def is_euleriano(grafo):
    """
    :param grafo:
    :param grafo:
    :return:
    """
    return not has_vertices_grau_impar(grafo)


def has_vertices_grau_impar(grafo):
    """
    :param grafo:
    :return: Algum dos vértices do grafo possui grau ímpar?
    """
    for vertice in grafo:
        if grafo.grau(vertice) % 2 == 1:
            return True

    return False


def buscar_tour_euleriana(grafo):
    """
    Usaremos o algoritmo de Fleury. O algoritmo detecta tours e caminhos
    eulerianos. Entretanto, queremos somente grafos eulerianos.

    O algoritmo de Fleury consiste resumidamente no passos:
     - https://www.math.ku.edu/~jmartin/courses/math105-F11/Lectures/chapter5-part2.pdf
       (slide 64)

    1. Make sure the graph has either 0 or 2 odd vertices.
    2. If there are 0 odd vertices, start anywhere. If there are 2
       odd vertices, start at one of them.
    3. Follow edges one at a time. If you have a choice between
       a bridge and a non-bridge, always choose the non-bridge.
    4. Stop when you run out of edges.
    """
    vertice = list(grafo.vertices)[0]

    return buscar_elemento_euleriano(vertice, grafo)


def buscar_elemento_euleriano(origem, grafo):
    # Se não copiar, como são excluídas arestas do grafo
    # que estamos iterando, dá o erro:
    #  RuntimeError: Set changed size during iteration
    copia_arestas = set(grafo[origem])

    for destino in copia_arestas:
        if not is_seguro(grafo, origem, destino):
            continue

        aresta = (origem, destino)
        grafo.remover_aresta(origem, destino)
        return [aresta] + buscar_elemento_euleriano(destino, grafo)

    return []


def is_seguro(grafo, origem, destino):
    origem_so_possui_um_adjacente = grafo.grau(origem) == 1
    return origem_so_possui_um_adjacente or not grafo.is_ponte(origem, destino)


def formatar_caminho(caminho):
    caminho_string = ''
    for aresta in caminho:
        vertice_origem, vertice_destino = aresta
        caminho_string += '{} -> '.format(vertice_origem, vertice_destino)

    return caminho_string + caminho[-1][1]

#######
# Main
#######
if __name__ == '__main__':
    grafo = ler_grafo_input()
    #grafo = ler_grafo_arquivo('exemplos/jurkiewicz.txt')

    if not is_euleriano(grafo):
        raise Exception("Grafo não é euleriano")

    caminho = buscar_tour_euleriana(grafo)

    print(formatar_caminho(caminho))
