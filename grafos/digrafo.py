from .grafo import Grafo

class Digrafo(Grafo):
    def __init__(self, num_vertices, ponderado=True):
        super().__init__(num_vertices, ponderado)

    def add_aresta(self, x, y, peso=1, direcionado=True):
        return super().add_aresta(x, y, peso, direcionado)
    
    def n(self):
        return super().n()
    
    def m(self):
        return sum(len(adj) for adj in self.lista_adjacencia.values())

    def viz(self, x):
        inneighborhood = []  

        for i in range(1, self.num_vertices + 1):
            for adjacente in self.lista_adjacencia[i]:
                if adjacente[0] == x:  
                    inneighborhood.append(i)  
                    break  

        outneighborhood = [] 
        
        for adjacente in self.lista_adjacencia[x]:
            outneighborhood.append(adjacente[0])

        return inneighborhood + outneighborhood
    
    def d(self, x):
        in_degree = 0
        for i in range(1, self.num_vertices + 1):
            for adjacente in self.lista_adjacencia[i]:
                if adjacente[0] == x:
                    in_degree += 1
                    break  

        out_degree = len(self.lista_adjacencia[x])
        
        return in_degree + out_degree
    
    def w(self, x, y):
        return super().w(x, y)
    
    def mind(self):
        return super().mind()
    
    def maxd(self):
        return super().maxd()
    
    def bfs(self, v):
        return super().bfs(v)
    
    def dfs(self, v):
        return super().dfs(v)
    
    def bf(self, v):
        return super().bf(v)
    
    def dijkstra(self, v):
        return super().dijkstra(v)
    
    def __str__(self):
        return super().__str__()
