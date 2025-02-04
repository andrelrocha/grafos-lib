class Grafo:
    def __init__(self, num_vertices, ponderado=True):
        self.num_vertices = num_vertices
        self.ponderado = ponderado
         #cria um dicionário onde cada chave e um vértice do grafo e o valor e uma lista dos vertices adjacentes a ele
        self.lista_adjacencia = {i: [] for i in range(1, num_vertices + 1)} 
        self.graus = []
        for _ in range(num_vertices + 1):
            self.graus.append(0)