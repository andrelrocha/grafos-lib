# Biblioteca de Grafos em Python

Este projeto tem como objetivo desenvolver uma biblioteca em Python que implementa estruturas de dados para grafos e dígrafos. A biblioteca contém duas classes principais: `Grafo` e `Digrafo`, que podem ser implementadas utilizando matriz de adjacência ou lista de adjacência. Além disso, a biblioteca permite ao usuário escolher qual das duas implementações utilizar. As classes incluem suporte para pesos nas arestas, com peso unitário (= 1) caso o grafo não seja ponderado.

## Estrutura do Projeto

- **Grafo**: Classe que representa um grafo não direcionado.
- **Digrafo**: Classe que representa um grafo direcionado (dígrafo).
- **Teste**: Conjunto de casos de teste para validar a implementação da biblioteca.

## Implementação

A biblioteca foi implementada utilizando lista de adjacência, onde cada vértice é representado por um índice em um dicionário, e o valor associado a cada vértice é uma lista de tuplas que representam os vértices adjacentes e os pesos das arestas. Essa abordagem é eficiente em termos de espaço e permite operações rápidas para grafos esparsos.

## Estrutura da Lista de Adjacência

A lista de adjacência é um dicionário onde cada chave é um vértice do grafo e o valor associado a cada chave é uma lista de tuplas (vértice_adjacente, peso_da_aresta).

Exemplo de representação:

```
{
    1: [(2, 5), (3, 2)],  # Vértice 1 está conectado ao vértice 2 com peso 5 e ao vértice 3 com peso 2
    2: [(1, 5), (4, 1)],  # Vértice 2 está conectado ao vértice 1 com peso 5 e ao vértice 4 com peso 1
    3: [(1, 2)],          # Vértice 3 está conectado apenas ao vértice 1 com peso 2
    4: [(2, 1)]           # Vértice 4 está conectado apenas ao vértice 2 com peso 1
}
```

## Casos de Teste

Para validar a biblioteca, foram realizados testes em uma instância real de um dígrafo que modela uma rede de estradas em Nova York, extraído da competição “9th DIMACS Implementation Challenge - Shortest Paths”. O dígrafo possui 264.346 vértices e 733.846 arcos, e é descrito no arquivo `USA-road-d.NY`.

### Descrição do Arquivo de Entrada

- **Formato**: As primeiras 7 linhas do arquivo correspondem ao cabeçalho. Cada linha subsequente corresponde a um arco no formato `a x y p`, onde:
  - `a` indica que se trata de um arco.
  - `x` é o vértice de origem.
  - `y` é o vértice de destino.
  - `p` é o peso do arco, que corresponde à distância real entre as localizações de `x` e `y`.

### Casos de Teste Realizados

1. **G.mind**: O valor mínimo de distância entre dois vértices no grafo.
2. **G.maxd**: O valor máximo de distância entre dois vértices no grafo.
3. **Caminho com pelo menos 10 arestas**: Um caminho no grafo com uma quantidade de arestas maior ou igual a 10, apresentando a sequência dos vértices.
4. **Ciclo com pelo menos 5 arestas**: Um ciclo no grafo com uma quantidade de arestas maior ou igual a 5, apresentando a sequência dos vértices.
5. **Vértice mais distante do vértice 129**: O vértice mais distante do vértice 129, considerando os pesos das arestas, e o valor da distância entre eles.

## Como Usar

1. **Instalação**: Clone o repositório e instale as dependências necessárias.
   ```bash
   git clone https://github.com/seu-usuario/biblioteca-grafos.git
   cd biblioteca-grafos
   pip install -r requirements.txt

