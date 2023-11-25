import math


class Grafo:
    def __init__(self, n):
        self.n = n  
        self.m = 0
        self.pesos = {}  
        self.nomes = {}
        self.listaAdj = [[] for i in range(self.n)]

    def escreverArquivo(self, arq):
        with open(arq, 'r') as f:
            content = []
            content.append(str(2)+'\n')
            content.append(str(self.n) + '\n')
           
            for i in self.nomes:
                content.append(str(i) + ' ' + self.nomes[i] + '\n')

            content.append(str(self.m) + '\n')

            listaAux = []
            indexAux = self.n + 3
            print(indexAux)
            print(content)

            for i, valor in self.pesos.items():
                if i[1] > i[0]: 
                    listaAux.append((i, valor))
                    content.append(str(listaAux[0][0]).replace("(", "").replace(")", "").replace(",","") + ' ' + str(listaAux[0][1]) + '\n')
                    indexAux += 1
                    listaAux.clear()

        with open(arq, 'w') as f:
            f.writelines(content)

    def insereVertice(self, v):
        lista = []
        idVertice = self.n

        for i in self.nomes:
            if v == self.nomes[i]:
                print("Vértice já existente.")
                return
            
        self.nomes[idVertice] = v
        self.listaAdj.append(lista)
        self.n += 1

        print(f"\nVértice adicionado com sucesso.")

    def removerVertice(self, v):
        if v not in self.nomes.values():
            print(f"Vértice {v} não encontrado.")
            return

        for i in range(self.n):
            if self.nomes[i] == v:
                for adjacente in self.listaAdj[i]:
                    self.listaAdj[adjacente].remove(i)
                    del self.pesos[i, adjacente]
                    del self.pesos[adjacente, i]

        indice_v = None
        for i in range(self.n):
            if self.nomes[i] == v:
                indice_v = i
                break
            
        chaves = list(self.nomes.keys())

        id_removido = None

        for chave in chaves:
            id_vertice = self.nomes[chave]
            if id_vertice == v:
                id_removido = chave
                break

        if id_removido is not None:
            for chave in chaves:
                if chave > id_removido:
                    novo_id = chave - 1
                    self.nomes[novo_id] = self.nomes[chave]
                    del self.nomes[chave]
            del self.listaAdj[id_removido]


            for i in range(len(self.listaAdj)):

                if i >= id_removido:
                    for j in range(len(self.listaAdj[i])):
                        novo = self.listaAdj[i][j] - 1
                        self.listaAdj[i][j] = novo

        else:
            print(f"Vértice {v} não encontrado.")
        
        if indice_v is not None:
            chaves = list(self.pesos.keys())
            for chave in chaves:
                (valor1, valor2) = chave 
                if valor1 > indice_v or valor2 > indice_v:
                    novo_valor1 = valor1 if valor1 <= indice_v else valor1 - 1
                    novo_valor2 = valor2 if valor2 <= indice_v else valor2 - 1
                    valor = self.pesos[chave]
                    del self.pesos[chave]
                    nova_chave = (novo_valor1, novo_valor2)
                    self.pesos[nova_chave] = valor

        self.n -= 1
        print(f"Vértice {v} removido com sucesso.")
        
    def insereAresta(self, v, w, peso, category):
        if category == 1:
            self.listaAdj[v].append(w)
            self.listaAdj[w].append(v)
            self.pesos[v, w] = peso   
            self.pesos[w, v] = peso
            self.m += 1
        else:
            for i in range(self.n):
                if self.nomes[i] == v:
                    indexV = i
                if self.nomes[i] == w:
                    indexW = i

            self.listaAdj[indexV].append(indexW)
            self.listaAdj[indexW].append(indexV)
            self.pesos[indexV, indexW] = peso   
            self.pesos[indexW, indexV] = peso
            self.m += 1
            print(f"Aresta entre {v} e {w} inserida com sucesso.")

    def removeAresta(self, v, w):
        if (v not in self.nomes.values()) or (w not in self.nomes.values()):
            print(f"Vértice {v} ou {w} não encontrado.")
            return
        
        for i in range(self.n):
            if self.nomes[i] == v:
                indexV = i
            if self.nomes[i] == w:
                indexW = i
        
        self.listaAdj[indexV].remove(indexW)
        self.listaAdj[indexW].remove(indexV)
        del self.pesos[indexV, indexW]
        del self.pesos[indexW, indexV]
        self.m -= 1
        print(f"Aresta entre {v} e {w} removida com sucesso.")


    def show(self):
        print(f"\n número de vértices:{self.n:2d}", end="")
        print(f"\n número de arestas:{self.m:2d}")

        vertices_validos = [i for i in range(self.n)]
        index = 0
        for i in vertices_validos:
            vertex_name = self.nomes[i]
            print(f"\n{vertex_name}", end="")
            for neighbor in self.listaAdj[index]:
                if (neighbor >= self.n) or (neighbor < 0):
                    continue
                neighbor_name = self.nomes[neighbor]
                if index == neighbor:
                    continue
                print(f" <--{self.pesos[i, neighbor]}--> {neighbor_name}", end="")
            index += 1

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
    
    def coloracao_sequencial(self):
        cores = [-1] * self.n  # Inicializa todas as cores como -1 (não atribuídas)

        for vertice in range(self.n):
            cores_disponiveis = set(range(self.n))

            for vizinho in self.listaAdj[vertice]:
                if cores[vizinho] != -1:
                    cores_disponiveis.discard(cores[vizinho])

            cor = min(cores_disponiveis)
            cores[vertice] = cor

        self.imprimir_coloracao(cores)

    def imprimir_coloracao(self, cores):
        mesmasCores = {}
        for vertice, cor in enumerate(cores):
            mesmasCores.setdefault(cor, []).append(vertice)

        for cor, vertices in mesmasCores.items():
            print(f"Cor {cor}:")
            for vertice in vertices:
                nome_vertice = self.nomes.get(vertice, f"Vértice {vertice}")
                print(f"  {nome_vertice}")

    def grauVertice(self, vertice):
        return len(self.listaAdj[vertice])
    
    def imprimirGrauVertices(self):
        for vertice in range(self.n):
            grau = self.grauVertice(vertice)
            print(f"Vértice: {vertice} Grau: {grau}\n")

    def grafoEuleriano(self):
        grauImpar = 0

        for vertice in self.listaAdj:
            if len(vertice) % 2 != 0:
                grauImpar += 1

        return grauImpar == 0 or grauImpar == 2
        
    def percursoEuleriano(self):
        if not self.busca_profundidade(0):
            return False

        graus_impares = 0
        for vertice in range(self.n):
            if self.grauVertice(vertice) % 2 != 0:
                graus_impares += 1


        return graus_impares == 0 or graus_impares == 2
    
    def grafoHamiltoniano(self):
        if self.n < 3:
            return True

        if not self.busca_profundidade(0):
            print("O grafo não é Hamiltoniano.")
            return False

        for i in range(self.n):   # Teorema de Ore
            for j in range(i + 1, self.n):
                if i not in self.listaAdj[j] and self.grauVertice(i) + self.grauVertice(j) < self.n:
                    print("O grafo não é Hamiltoniano.")
                    return False

        print("O grafo pode ser Hamiltoniano.")
        return True