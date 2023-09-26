"""
    Mateus Fernandes Castanharo - 32137141
    Victor Hugo Antonio Couto - 32173482
"""


class Grafo:
    # construtor da classe grafo

    def __init__(self, n):
        self.n = n  # número de vértices
        self.m = 0  # número de arestas
        self.typeGraph = 0
        self.pesos = {}  # pesos de cada aresta
        self.nomes = {}
        # lista de adjacência
        self.listaAdj = [[] for i in range(self.n)]



    def insereVertice(self, v):
        idVertice = self.n + 1
        self.nomes[idVertice] = v;
        print(f'Lista: {self.n}')

        for i in self.nomes:
            if v == self.nomes[i]:
                print("Vértice já existente.")
                return
        
        self.n += 1
        print(f'AAA: {self.n}')
        self.listaAdj.append(idVertice)
        print("Vértice adicionado com sucesso.")


        # Insere uma aresta no Grafo tal que
        # v é adjacente a w
    def insereAresta(self, v, w, peso):
        #print(self.listaAdj)
        # for (i,j) in self.listaAdj:
        #     if (i,j) == (v,w):
        #         print("Aresta existente.")
        #         return


        self.listaAdj[v].append(w)
        self.listaAdj[w].append(v)
        self.pesos[v, w] = peso     # Guarda na lista de pesos
        self.pesos[w, v] = peso
        self.m += 1


    def removeVertice(self, v, w):
        self.listaAdj[v].remove(w)
        self.listaAdj[w].remove(v)
        del self.pesos[v, w]
        del self.nomes[v]
        self.n -= 1
        self.m -=1

    # remove uma aresta v->w do Grafo
    def removeAresta(self, v, w):
        self.listaAdj[v].remove(w)
        self.listaAdj[w].remove(v)
        del self.pesos[v,w]         # Remove da lista de pesos
        self.m -= 1


        # Apresenta o Grafo contendo
        # número de vértices, arestas
        # e a LISTA de adjacência obtida
    def show(self):
        print(f"\n n:{self.n:2d}", end="")
        print(f" m:{self.m:2d}")
        for i in range(self.n):
            if i == 0:
                continue
            else:
                print(f"\n{self.nomes[i-1]}", end="")
            for w in range(len(self.listaAdj[i])):
                val = self.listaAdj[i][w]
                # printa pesos de cada aresta
                print(
                    f" <--{self.pesos[i,val]}--> {self.nomes[val-1]}", end="")

        print("\n\nfim da impressao do grafo.")

    def busca_profundidade(self, vertice_inicial):
            visitados = set()

            def dfs(vertice):
                visitados.add(vertice)
                for vizinho in self.listaAdj[vertice]:
                    if vizinho not in visitados:
                        dfs(vizinho)

            dfs(vertice_inicial)
            return visitados