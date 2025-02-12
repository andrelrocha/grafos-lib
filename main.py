from grafos.grafo import Grafo
from grafos.digrafo import Digrafo

def main():
    print("Testes de Grafo e Digrafo")
    print("Grafo não direcionado")
    g = Grafo(5)
    g.add_aresta(1, 2, 2)
    g.add_aresta(1, 3, 3)
    g.add_aresta(2, 3)
    g.add_aresta(3, 4)
    g.add_aresta(4, 5)
    g.add_aresta(5, 1)
    print(g.n(), g.m())

    print("Digrafo direcionado")
    d = Digrafo(5)
    d.add_aresta(1, 2, 10)
    d.add_aresta(1, 3, 5)
    d.add_aresta(2, 3)
    d.add_aresta(3, 4)
    d.add_aresta(4, 5)
    d.add_aresta(5, 1)
    print(d.n(), d.m()) 

    print("Vizinhança do Grafo 1")
    print(g.viz(1))

    print("Vizinhança do Digrafo 1")
    print(d.viz(1))

    print("Grau do vértice 1 no Grafo")
    print(g.d(1))

    print("Grau do vértice 1 no Digrafo")
    print(d.d(1))

    print("Peso da aresta 2-1 no Grafo")
    print(g.w(2, 1))

    print("Peso da aresta 2-1 no Digrafo")
    print(d.w(2, 1))

    print("Vértice de menor grau no Grafo")
    print(g.mind())
    print("Vértice de menor grau no Digrafo")
    print(d.mind())
    print("Vértice de maior grau no Grafo")
    print(g.maxd())
    print("Vértice de maior grau no Digrafo")
    print(d.maxd())

    print("BFS no Grafo a partir do vértice 1")
    d_grafo, pi_grafo = g.bfs(1)
    print("Distâncias:", d_grafo)
    print("Pais:", pi_grafo)

    print("BFS no Digrafo a partir do vértice 1")
    d_digrafo, pi_digrafo = d.bfs(1)
    print("Distâncias:", d_digrafo)
    print("Pais:", pi_digrafo)



if __name__ == "__main__":
    main()