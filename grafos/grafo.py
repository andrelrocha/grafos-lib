class Grafo:
    def __init__(self, num_vertices, ponderado=True):
        self.num_vertices = num_vertices
        self.ponderado = ponderado
         #cria um dicionário onde cada chave e um vértice do grafo e o valor e uma lista dos vertices adjacentes a ele
        self.lista_adjacencia = {i: [] for i in range(1, num_vertices + 1)} 
        self.graus = []
        for _ in range(num_vertices + 1):
            self.graus.append(0)

    def add_aresta(self, x, y, peso = 1, direcionado = False):
        if not self.ponderado:
            peso = 1

        self.lista_adjacencia[x].append((y, peso))
        if not direcionado:
            self.lista_adjacencia[y].append((x, peso))

        self.graus[x] += 1
        self.graus[y] += 1

    def n(self):
        return self.num_vertices
    
    def m(self):
        total_arestas = sum(len(adj) for adj in self.lista_adjacencia.values())
        return total_arestas // 2

    def viz(self, x):
        lista_adjacente = self.lista_adjacencia[x]
        vertices_adjacentes = []
        
        for adj in lista_adjacente:
            vertices_adjacentes.append(adj[0])
        
        return vertices_adjacentes
    
    def d(self, x):
        # O grau de um vértice é o número de arestas incidentes a ele
        return len(self.lista_adjacencia[x])

