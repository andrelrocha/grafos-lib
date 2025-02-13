from grafos.digrafo import Digrafo

def parse_digrafo(file_path, num_vertices):
    try:
        digrafo = Digrafo(num_vertices, ponderado=True)

        with open(file_path, 'r') as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if not line.startswith('a'):
                    continue
                parts = line.split()
                if len(parts) < 4:
                    continue
                x, y, p = map(int, parts[1:4])

                digrafo.add_aresta(x, y, p, direcionado=True)

        return digrafo
    except FileNotFoundError:
        print(f"O arquivo {file_path} não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")

if __name__ == "__main__":
    file_path = "docs/USA-road-d.NY.gr"  
    num_vertices = 264346                
    digrafo = parse_digrafo(file_path, num_vertices)
