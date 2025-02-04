from grafo import Grafo

class Digrafo(Grafo):
    def __init__(self, num_vertices, ponderado=True):
        super().__init__(num_vertices, ponderado)