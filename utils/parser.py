from grafos.digrafo import Digrafo

def parse_digrafo(file_path):
    try:
        digrafo = Digrafo()

        with open(file_path, 'r') as f:
            # Ler todas as linhas do arquivo
            lines = f.readlines()

            # Inicializar a lista de adjacência do Digrafo
            digrafo.lista_adjacencia = [[] for _ in range(264347)]  # 264346 vértices + 1 para indexar a partir de 1
            digrafo.num_arcos = 0  # Contagem de arcos

            # Percorrer as linhas
            for line in lines:
                line = line.strip()
                if line.startswith('a'):  # Se a linha começa com 'a', é um arco
                    parts = line.split()
                    x = int(parts[1])  # Vértice de origem
                    y = int(parts[2])  # Vértice de destino
                    p = int(parts[3])  # Peso do arco

                    # Adicionar arco direcionado (digrafo)
                    digrafo.lista_adjacencia[x].append((y, p))  # x -> y com peso p

                    # Incrementar número de arcos
                    digrafo.num_arcos += 1

        return digrafo

    except FileNotFoundError:
        print(f"O arquivo {file_path} não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")
