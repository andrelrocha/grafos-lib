from utils.parser import parse_digrafo

class TestesDigrafo:

    def __init__(self, arquivo, num_vertices):
        # Carregar o digrafo a partir do arquivo
        self.digrafo = parse_digrafo(arquivo, num_vertices)  # Agora, armazene o digrafo no atributo self.digrafo

    def executar_testes(self):
        # Teste a menor distância
        print("chamou nos testes")


        ##TÁ DANDO ERRO AQUI EM MIND
        print(self.digrafo.mind())
        """
        mind = self.digrafo.mind()
        print(f"a) Menor distância: {mind}")

        # Teste a maior distância
        maxd = self.digrafo.maxd()
        print(f"b) Maior distância: {maxd}")

        # Teste um caminho com mais de 10 arestas
        caminho_longo = self.digrafo.bfs(1)  # Exemplo com busca em largura (bfs)
        print(f"c) Caminho com mais de 10 arestas: {caminho_longo[:10]}")  # Limitando a 10 arestas

        # Teste um ciclo com mais de 5 arestas (considerando a lógica de ciclo)
        ciclo_longo = self.digrafo.dfs(1)  # Exemplo com busca em profundidade (dfs)
        print(f"d) Ciclo com mais de 5 arestas: {ciclo_longo[:5]}")  # Limitando a 5 arestas

        # Teste o vértice mais distante do vértice 129
        vertice_mais_distante, distancia = self.digrafo.dijkstra(129)
        print(f"e) Vértice mais distante de 129: {vertice_mais_distante}, Distância: {distancia}")
        """
        
        
# Exemplo de execução dos testes
if __name__ == "__main__":
    arquivo = 'USA-road-d.NY'  # Caminho do arquivo de entrada
    num_vertices = 264347  # Ou o número real de vértices do seu grafo
    testes = TestesDigrafo(arquivo, num_vertices)  # Agora você passa o arquivo e num_vertices
    testes.executar_testes()
