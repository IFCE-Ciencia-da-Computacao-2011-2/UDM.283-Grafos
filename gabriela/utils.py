def vertices_conexos_a_partir_de(no, grafo):
    """
    :param no: nó inicial do grafo que será realizada a busca
    """
    return _dfs(grafo, no, set())


def _dfs(grafo, no, visitados):
    """
    :param no: no inicial do grafo
    :param grafo: contêm todos os pares de arestas e vertices do grafo
    :param visitas: lista de vértices sem repetião da busca
    """
    if no in visitados:
        return visitados

    visitados |= {no}
    for destino in grafo[no]:
        visitados = _dfs(grafo, destino, visitados)

    return visitados
