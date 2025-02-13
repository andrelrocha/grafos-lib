from testes.teste import TestesDigrafo

def main():
    print("Executando o script principal...")

    # Caminho do arquivo de entrada
    arquivo = 'docs/USA-road-d.NY.gr'

    # Criando a instância de TestesDigrafo com o arquivo
    testes = TestesDigrafo(arquivo, 264346)

    print("Executando os testes...")

    # Executando os testes
    testes.executar_testes()

if __name__ == "__main__":
    main()