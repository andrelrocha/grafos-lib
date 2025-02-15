from utils.parser import parse_digrafo

class TestesDigrafo:
    def __init__(self, arquivo, num_vertices):
        self.digrafo = parse_digrafo(arquivo, num_vertices) 

    def encontrar_caminho_10_arestas(self):
        d, pi = self.digrafo.bfs(1) 
        for destino, dist in d.items():
            if dist >= 10: 
                caminho = []
                atual = destino
                while atual is not None:
                    caminho.append(atual)
                    atual = pi[atual]
                caminho.reverse()  
                print(f"c) Primeiro caminho com mais de 10 arestas: {caminho[:10]}")  
                break

    def encontrar_ciclo_minimo_5_arestas(self):
        pi, x_ini, x_fim = self.digrafo.dfs(1)

        def reconstruir_ciclo(vertice, vizinho, pi):
            ciclo = []
            x = vertice
            while x != vizinho:
                ciclo.append(x)
                x = pi[x]
                if x is None:
                    return None
            ciclo.append(vizinho)
            ciclo.append(vertice)
            return ciclo[::-1] 

        for vertice in self.digrafo.lista_adjacencia:
            for vizinho, _ in self.digrafo.lista_adjacencia[vertice]:
                if x_ini[vertice] > x_ini[vizinho] and x_fim[vertice] < x_fim[vizinho]: #procura por arestas de retorno
                    ciclo = reconstruir_ciclo(vertice, vizinho, pi)
                    if len(ciclo) > 5: 
                        print(f"d) Ciclo com pelo menos 5 arestas: {ciclo}")
                        return ciclo
    
    def encontrar_vertice_mais_distante(self, x):
        d, pi = self.digrafo.dijkstra(x)

        vertice_mais_distante = None 
        maior_distancia = 0   

        for v, distancia in d.items():
            if distancia != float('inf') and distancia > maior_distancia:
                vertice_mais_distante = v
                maior_distancia = distancia

        print(f"e) Vértice mais distante do vértice 129: {vertice_mais_distante} com distância total {maior_distancia}")
        
    def executar_testes(self):
        print("Iniciada a chamada do método executar_testes()")

        mind = self.digrafo.mind()
        print(f"a) Menor grau: {mind}")

        maxd = self.digrafo.maxd()
        print(f"b) Maior grau: {maxd}")

        self.encontrar_caminho_10_arestas()

        self.encontrar_ciclo_minimo_5_arestas()

        self.encontrar_vertice_mais_distante(129)

        #print(self.digrafo)  