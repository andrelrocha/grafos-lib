from grafos.digrafo import Digrafo

def parse_digrafo(path, num_vertices):
    try:
        digrafo = Digrafo(num_vertices, ponderado=True)

        with open(path, 'r') as f:
            linhas = f.readlines()
            for linha in linhas:
                linha = linha.strip()
                if not linha.startswith('a'):
                    continue
                parts = linha.split()
                if len(parts) < 4:
                    continue
                x, y, p = map(int, parts[1:4])

                digrafo.add_aresta(x, y, p, direcionado=True)

        return digrafo
    except FileNotFoundError:
        print(f"O arquivo {path} não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")

if __name__ == "__main__":
    path = "docs/USA-road-d.NY.gr"  
    num_vertices = 264346                
    digrafo = parse_digrafo(path, num_vertices)
