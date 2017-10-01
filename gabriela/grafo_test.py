import unittest


from ler_entrada import *
from programa import *
from grafo import Grafo


class TestGrafoTest(unittest.TestCase):

    def test_has_vertices_grau_impar(self):
        grafo_sem_impar = ler_grafo_arquivo('exemplos/jurkiewicz.txt')
        grafo_com_impar = ler_grafo_arquivo('exemplos/video_wA2rKfByLAY.txt')

        self.assertFalse(has_vertices_grau_impar(grafo_sem_impar))
        self.assertTrue(has_vertices_grau_impar(grafo_com_impar))

    def test_is_ponte_aresta_nao_pertencente_ao_grafo(self):
        grafo = Grafo()
        grafo.adicionar_aresta(1, 2)
        grafo.adicionar_aresta(2, 3)

        with self.assertRaises(Exception):
            grafo.is_ponte(1, 3)

    def test_bug(self):
        grafo = Grafo()
        grafo.adicionar_aresta('B', 'C')
        grafo.adicionar_aresta('B', 'A')
        grafo.adicionar_aresta('A', 'E')
        grafo.adicionar_aresta('A', 'F')
        grafo.adicionar_aresta('F', 'E')

        self.assertTrue(grafo.is_conexo())

        grafo.remover_aresta('A', 'B')
        self.assertFalse(grafo.is_conexo())
        grafo.adicionar_aresta('A', 'B')

        grafo.remover_aresta('A', 'F')
        self.assertTrue(grafo.is_conexo())
        grafo.adicionar_aresta('A', 'F')

        grafo.remover_aresta('A', 'E')
        self.assertTrue(grafo.is_conexo())
        grafo.adicionar_aresta('A', 'E')

    def test_bug_2(self):
        grafo = Grafo()
        grafo.adicionar_aresta('B', 'A')
        grafo.adicionar_aresta('A', 'E')
        grafo.adicionar_aresta('A', 'F')
        grafo.adicionar_aresta('F', 'E')

        grafo.remover_aresta('A', 'E')
        self.assertTrue(grafo.is_conexo())

    def test_bug_3(self):
        grafo = ler_grafo_arquivo('exemplos/jurkiewicz.txt')
        grafo.remover_aresta('F', 'A')
        grafo.remover_aresta('A', 'E')

        origem, destino = 'E', 'F'

        self.assertEqual(grafo.grau(destino), 1)
        self.assertTrue(grafo.is_ponte(origem, destino))

        self.assertFalse(is_seguro(grafo, origem, destino))
        #grafo.remover_aresta(origem, destino)

    def teste_arquivos(self):
        self.verificar_arquivo('exemplos/video_wA2rKfByLAY.txt')
        self.verificar_arquivo('exemplos/jurkiewicz.txt')
        self.verificar_arquivo('exemplos/entrada.txt')
        self.verificar_arquivo('exemplos/nao_conexo.txt')
        self.verificar_arquivo('exemplos/euleriano.txt')
        self.verificar_arquivo('exemplos/grafo_com_ponte.txt')

    def verificar_arquivo(self, arquivo):
        grafo = ler_grafo_arquivo(arquivo)
        total_arestas = grafo.total_arestas

        if not is_euleriano(grafo):
            print(arquivo, 'não é euleriano')
            return

        caminho = buscar_tour_euleriana(grafo)
        print(arquivo, formatar_caminho(caminho))

        self.assertEqual(total_arestas, len(caminho))

if __name__ == '__main__':
    unittest.main()
