"""
    Mateus Fernandes Castanharo - 32137141
    Victor Hugo Antonio Couto - 32173482

    O projeto consiste em representar a rota comercial da seda, uam das rotas mais famosas durante a idade média, 
    durante o século XIV, utilizando os conceitos de teoria dos grafos. 
    O grafo modulado contém as principais cidades que faziam parte, que contemplam os continentes: Europa e Ásia,
    e as respectivas distância aproximadas entre as cidades.
    
    O principal objetivo do projeto é de fornecer informações sobre a rota da seda de uma maneira dinâmica e intuitiva.

"""


from grafoImp import Grafo
import time


def grafoArq(file):
    with open(file) as f:
        content = f.readlines()  # Salva arquivo inteiro
        tipoGrafo = int(content[0])  # Primeira linha do arquivo
        qtdVertices = int(content[1])  # Segunda linha do arquivo
        qtdArestas = int(content[qtdVertices+2])  # Arestas
        vertices = []  # Todos os vertices
        arestas = []   # Todas as arestas

        # loop do primeiro vertice até o ultimo
        for line in range(2, qtdVertices+2):
            vertices.append(content[line].split(" "))  # Guarda em uma lista

        # loop do final dos vertices até o final do arquivo
        for line in range(qtdVertices+3, len(content)):
            arestas.append(content[line].split(" "))   # Guarda em uma lista

        # Cria o grafo com todos os vertices
        g = Grafo(qtdVertices)

        for i in range(qtdVertices):  # armazena os nomes
            g.nomes[i] = vertices[i][1].rstrip('\n')

        for i in range(qtdArestas):  # Adiciona todas as arestas e pesos

            g.insereAresta(int(arestas[i][0]), int(
                arestas[i][1]), int(arestas[i][2]), 1)

        g.typeGraph = tipoGrafo
        print("Arquivo lido com sucesso.")

        return g


def writeFile(graph):
    graph.escreverArquivo("grafo.txt")


def inserirVertice(graph):
    nomeVertice = input("Informe o nome do vértice: ")
    graph.insereVertice(nomeVertice)


def inserirAresta(graph):
    verticeOrigem = input("Vértice de origem: ")
    verticeDestino = input("Vértice de destino: ")
    peso = int(input("Peso da aresta: "))
    graph.insereAresta(verticeOrigem, verticeDestino, peso, 4)

def removerVertice(graph):
    nomeVertice = input("Informe o nome do vértice: ")
    graph.removerVertice(nomeVertice)

def removerAresta(graph):
    verticeOrigem = input("Vértice de origem: ")
    verticeDestino = input("Vértice de destino: ")
    graph.removeAresta(verticeOrigem, verticeDestino)


def showContent(graph):
    print(f"Conteúdo do arquivo:\nNúmero de vértices: {graph.n}.\nNúmero de arestas: {graph.m}.\nCidades: {graph.nomes}.\nDistância entre as cidades: {graph.pesos}.\n\n")


    match graph.typeGraph:
        case 0:
            print("Grafo não orientado sem peso!")
        case 1:
            print("Grafo não orientado com peso no vértice!")
        case 2:
            print("Grafo não orientado com peso na aresta!")
        case 3:
            print("Grafo não orientado com peso nos vértices e arestas!")
        case 4:
            print("Grafo orientado sem peso!")
        case 5:
            print("Grafo orientado com peso no vértice!")
        case 6:
            print("Grafo orientado com peso na aresta!")
        case 7:
            print("Grafo orientado com peso nos vértices e arestas!")
        case _:
            print("Não é uma opção valida")
            exit()


def conexidadeGrafo(graph):
    print("Conexidade do grafo: ", end="")
    if len(graph.busca_profundidade(1)) != graph.n:
        print("Grafo é desconexo!")
    else:
        print("Grafo é conexo!")

def coloracaoGrafo(graph):
    print("Coloração do grafo:\n")
    graph.coloracao_sequencial()

def euleriano(graph):
    print("O grafo é Euleriano" if graph.grafoEuleriano() == 1 else "O grafo não é Euleriano.")

def perEuleriano(graph):
    print("O grafo possui percurso Euleriano" if graph.percursoEuleriano() == 1 else "O grafo não possui percurso Euleriano.")

def grauDosvertices(graph):
    graph.imprimirGrauVertices()

def hamiltoniano(graph):
    print("O grafo é Hamiltoniano" if graph.grafoHamiltoniano() == 1 else "O grafo não é Hamiltoniano.")
    


def menu():
    graph = 0
    while(True):
        print('\n\n', "<",  "-"*60, ">")
        print(" |", " "*5, "Mapeamento da rota da seda durante o século XIV", " "*6, "|", "\n", "|", "-"*60, "|", "\n",
              "|", " "*20, "Opções de operações: ", " " *
              17, "|", "\n", "|", "-"*60, "|", "\n",
              "|", " "*15, "1. Ler os dados do arquivo.", " " *
              16, "|", "\n", "|", "-"*60, "|", "\n",
              "|", " "*15, "2. Gravar dados no arquivo.", " " *
              16, "|", "\n", "|", "-"*60, "|", "\n",
              "|", " "*15, "3. Inserir vértice no Grafo.", " " *
              15, "|", "\n", "|", "-"*60, "|", "\n",
              "|", " "*15, "4. Inserir aresta no Grafo.", " " *
              16, "|", "\n", "|", "-"*60, "|", "\n",
              "|", " "*15, "5. Remover vértice do grafo.", " " *
              15, "|", "\n", "|", "-"*60, "|", "\n",
              "|", " "*15, "6. Remover aresta do grafo.", " " *
              16, "|", "\n", "|", "-"*60, "|", "\n",
              "|", " "*15, "7. Mostrar conteúdo do arquivo.", " " *
              12, "|", "\n", "|", "-"*60, "|", "\n",
              "|", " "*15, "8. Mostrar grafo.", " "*26, "|", "\n", "|", "-"*60, "|", "\n",
              "|", " "*15, "9. Conexidade do grafo.", " " *
              20, "|", "\n", "|", "-"*60, "|", "\n",
              "|", " "*15, "10. Coloração.", " " *
              29, "|", "\n", "|", "-"*60, "|", "\n",
              "|", " "*15, "11. Grau dos Vértices.", " " *
              21, "|", "\n", "|", "-"*60, "|", "\n",
              "|", " "*15, "12. Grafo Euleriano.", " " *
              23, "|", "\n", "|", "-"*60, "|", "\n",
              "|", " "*15, "13. Percurso Euleriano.", " " *
              20, "|", "\n", "|", "-"*60, "|", "\n",
              "|", " "*15, "14. Grafo Hamiltoniano.", " " *
              20, "|", "\n", "|", "-"*60, "|", "\n",
              "|", " "*15, "15. Encerrar.", " "*30, "|", "\n", "<", "-"*60, ">", "\n",
              )
        opcao = int(input("Escolha a opção: "))

        match opcao:
            case 1:
                graph = grafoArq("grafo.txt")
                time.sleep(1)
            case 2:
                writeFile(graph)
                time.sleep(1)
            case 3:
                inserirVertice(graph)
                time.sleep(1)
            case 4:
                inserirAresta(graph)
                time.sleep(1)
            case 5:
                removerVertice(graph)
                time.sleep(1)
            case 6:
                removerAresta(graph)
                time.sleep(1)
            case 7:
                showContent(graph)
                time.sleep(1)
            case 8:
                print("\n\n", "-"*20, "   Apresentação do grafo   ", "-"*20)
                graph.show()
                time.sleep(3)
            case 9:
                conexidadeGrafo(graph)
                time.sleep(1)
            case 10:
                coloracaoGrafo(graph)
                time.sleep(1)
            case 11:
                grauDosvertices(graph)
                time.sleep(1)
            case 12:
                euleriano(graph)
                time.sleep(1)
            case 13:
                perEuleriano(graph)
                time.sleep(1)
            case 14:
                hamiltoniano(graph)
                time.sleep(1)
            case 15:
                print("Fim do programa")
                time.sleep(1)
                break
            case _:
                print("Opção inválida!")
                time.sleep(1)

def main():
    menu()

main()
