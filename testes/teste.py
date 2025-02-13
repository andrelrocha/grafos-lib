from utils.parser import parse_digrafo

class TestesDigrafo:

    def __init__(self, arquivo, num_vertices):
        # Carregar o digrafo a partir do arquivo
        self.digrafo = parse_digrafo(arquivo, num_vertices)  # Agora, armazene o digrafo no atributo self.digrafo

    def encontrar_caminho_10_arestas(self):
        d, pi = self.digrafo.bfs(1)  # Executa BFS a partir do vértice 1
        for destino, dist in d.items():
            if dist >= 10:  # Encontrou o primeiro caminho com 10 ou mais arestas
                caminho = []
                atual = destino
                while atual is not None:
                    caminho.append(atual)
                    atual = pi[atual]
                caminho.reverse()  # Inverte para ficar na ordem correta
                print(f"c) Primeiro caminho com mais de 10 arestas: {caminho[:10]}")  # Limitando a 10 arestas
                break

    def encontrar_ciclo(self):
        def dfs_aux(v, pi, visitado, x_ini, x_fim, tempo):
            visitado.add(v)
            tempo[0] += 1
            x_ini[v] = tempo[0]

            for vizinho, _ in self.digrafo.lista_adjacencia[v]:
                if vizinho not in visitado:
                    pi[vizinho] = v
                    if dfs_aux(vizinho, pi, visitado, x_ini, x_fim, tempo):
                        return True
                elif pi[v] != vizinho:  # Detecta um ciclo
                    ciclo = self.reconstruir_ciclo(v, vizinho, pi)
                    if len(ciclo) - 1 >= 5:  # Verifica se o ciclo tem pelo menos 5 arestas
                        print(f"d) Primeiro ciclo com 5 ou mais arestas: {ciclo}")
                        return True
            tempo[0] += 1
            x_fim[v] = tempo[0]
            return False

        pi = {}  # Pai de cada vértice
        visitado = set()
        x_ini = {}
        x_fim = {}
        tempo = [0]

        for vertice in self.digrafo.lista_adjacencia:
            if vertice not in visitado:
                if dfs_aux(vertice, pi, visitado, x_ini, x_fim, tempo):
                    break  # Sai do loop se encontrar um ciclo

    def reconstruir_ciclo(self, v, vizinho, pi):
        # Começa a reconstrução a partir do vértice 'v'
        ciclo = [vizinho]
        atual = v
        # Segue a cadeia de predecessores até encontrar 'vizinho'
        while atual is not None and atual != vizinho:
            ciclo.append(atual)
            atual = pi.get(atual)  # Usa get() para evitar KeyError
        if atual is None:
            return []  # Não foi possível reconstruir o ciclo (deve ser ignorado)
        ciclo.append(vizinho)  # Fecha o ciclo
        ciclo.reverse()  # Inverte a ordem, se desejar
        return ciclo
    
    def encontrar_vertice_mais_distante(self):
        d, pi = self.digrafo.dijkstra(129)
        
        max_vertice = None
        max_distancia = 0
        for v, distancia in d.items():
            if distancia != float('inf') and distancia > max_distancia:
                max_vertice = v
                max_distancia = distancia

        if max_vertice is not None:
            print(f"Vértice mais distante do vértice 129: {max_vertice} com distância {max_distancia}")
        else:
            print(f"Não há vértices alcançáveis a partir do vértice 129.")
        
    def executar_testes(self):
        # Teste o menor grau
        print("Executando os testes...")
        mind = self.digrafo.mind()
        print(f"a) Menor grau: {mind}")

        # Teste o maior grau
        maxd = self.digrafo.maxd()
        print(f"b) Maior grau: {maxd}")

        # Teste do primeiro caminho com mais de 10 arestas
        self.encontrar_caminho_10_arestas()

        # Teste do primeiro ciclo com 5 ou mais arestas
        self.encontrar_ciclo()

        # Teste do vértice mais distante do vértice 129
        self.encontrar_vertice_mais_distante()
        
        
        
# Exemplo de execução dos testes
if __name__ == "__main__":
    arquivo = 'USA-road-d.NY'  # Caminho do arquivo de entrada
    num_vertices = 264347  # Ou o número real de vértices do seu grafo
    testes = TestesDigrafo(arquivo, num_vertices)  # Agora você passa o arquivo e num_vertices
    testes.executar_testes()
