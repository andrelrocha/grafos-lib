import heapq

class Grafo:
    def __init__(self, num_vertices, ponderado=True):
        self.num_vertices = num_vertices
        self.ponderado = ponderado
        #cria um dicionário onde cada chave e um vértice do grafo e o valor e uma lista dos vertices adjacentes a ele
        self.lista_adjacencia = {i: [] for i in range(1, num_vertices + 1)} 
        self.graus = []
        for _ in range(num_vertices + 1):
            self.graus.append(0)
        self.cor = ["branco"] * (num_vertices + 1) 
        self.pi = [None] * (num_vertices + 1) 

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
        return len(self.lista_adjacencia[x])

    def w(self, x, y):
        for adjacente in self.lista_adjacencia[x]:
            if adjacente[0] == y:  
                return adjacente[1] 

        print(f"não existe aresta entre {x} e {y}")
        return None

    def mind(self):
        if self.num_vertices == 0:
            return None

        return min(self.graus[1:])

    def maxd(self):
        if self.num_vertices == 0:
            return None 

        return max(self.graus[1:])
    
    def bfs(self, v):
        d = {}
        pi = {}

        for i in self.lista_adjacencia:
            d[i] = float('inf')  
            pi[i] = None 

        d[v] = 0

        fila = [v]

        while len(fila) > 0:
            u = fila.pop(0) 

            for vizinho, _ in self.lista_adjacencia[u]:
                if d[vizinho] == float('inf'):  
                    d[vizinho] = d[u] + 1 
                    pi[vizinho] = u
                    fila.append(vizinho)  

        return d, pi

    def dfs(self, x):
        tempo = [0]
        pi = {}
        x_ini = {}
        x_fim = {}
        cor = {} 

        for v in self.lista_adjacencia:
            pi[v] = None
            x_ini[v] = -1
            x_fim[v] = -1
            cor[v] = "branco"  

        pilha = [(x, "cinza")]  
        cor[x] = "cinza"
        x_ini[x] = tempo[0]
        tempo[0] += 1

        while len(pilha) > 0:
            vertice, status = pilha[-1]

            if status == "cinza": 
                todos_visitados = True
                for vizinho, _ in self.lista_adjacencia[vertice]:
                    if cor[vizinho] == "branco": 
                        pi[vizinho] = vertice
                        cor[vizinho] = "cinza" 
                        x_ini[vizinho] = tempo[0]
                        tempo[0] += 1
                        pilha.append((vizinho, "cinza"))  
                        todos_visitados = False
                        break  

                if todos_visitados:
                    pilha[-1] = (vertice, "preto") 

            elif status == "preto":
                x_fim[vertice] = tempo[0]
                tempo[0] += 1
                cor[vertice] = "preto" 
                pilha.pop()

        return pi, x_ini, x_fim

    def bf(self, v):
        d = {}  
        pi = {}  

        for i in range(1, self.num_vertices + 1):
            d[i] = float('inf')  
            pi[i] = None  
            
        d[v] = 0

        for _ in range(self.num_vertices - 1):
            for x in range(1, self.num_vertices + 1): 
                for y, peso in self.lista_adjacencia[x]:  
                    if d[x] != float('inf') and d[x] + peso < d[y]: 
                        d[y] = d[x] + peso
                        pi[y] = x

        for x in range(1, self.num_vertices + 1):
            for y, peso in self.lista_adjacencia[x]: 
                if d[x] != float('inf') and d[x] + peso < d[y]:  # Se for possível relaxar
                    print("ciclo negativo no grafo")
                    return

        return d, pi

    def dijkstra(self, v):
        d = {}  
        pi = {}  

        for i in range(1, self.num_vertices + 1):
            d[i] = float('inf')  
            pi[i] = None  


        d[v] = 0  

        min_heap = [(0, v)] 

        while len(min_heap) > 0:
            dist_x, x = heapq.heappop(min_heap) 

            if dist_x > d[x]:
                continue

            for adjacente, peso in self.lista_adjacencia[x]:
                # relaxamento da aresta
                if d[x] + peso < d[adjacente]:
                    d[adjacente] = d[x] + peso
                    pi[adjacente] = x
                    heapq.heappush(min_heap, (d[adjacente], adjacente)) 

        return d, pi

    def __str__(self):
        for i in self.lista_adjacencia:
            print(f"{i}: {self.lista_adjacencia[i]}")
        return ""

