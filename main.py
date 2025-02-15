from testes.teste import TestesDigrafo

def main():
    arquivo = 'docs/USA-road-d.NY.gr'
    num_vertices = 264346

    testes = TestesDigrafo(arquivo, num_vertices)
    testes.executar_testes()

if __name__ == "__main__":
    main()