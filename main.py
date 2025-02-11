from grafos.grafo import Grafo
from grafos.digrafo import Digrafo

def main():
    print("Testes de Grafo e Digrafo")
    print("Grafo não direcionado")
    g = Grafo(5)
    g.add_aresta(1, 2)
    g.add_aresta(1, 3)
    g.add_aresta(2, 3)
    g.add_aresta(3, 4)
    g.add_aresta(4, 5)
    g.add_aresta(5, 1)
    print(g.n(), g.m())

    print("Digrafo direcionado")
    d = Digrafo(5)
    d.add_aresta(1, 2)
    d.add_aresta(1, 3)
    d.add_aresta(2, 3)
    d.add_aresta(3, 4)
    d.add_aresta(4, 5)
    d.add_aresta(5, 1)
    print(d.n(), d.m()) 

    print("Vizinhança do Grafo 1")
    print(g.viz(1))

    print("Vizinhança do Digrafo 1")
    print(d.viz(1))


if __name__ == "__main__":
    main()