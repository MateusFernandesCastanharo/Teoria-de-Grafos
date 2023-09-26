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
        print(content)
        tipoGrafo = int(content[0])  # Primeira linha do arquivo
        qtdVertices = int(content[1])  # Segunda linha do arquivo
        qtdArestas = int(content[qtdVertices+1])  # Arestas
        vertices = []  # Todos os vertices
        arestas = []   # Todas as arestas

        # loop do primeiro vertice até o ultimo
        for line in range(2, qtdVertices+1):
            vertices.append(content[line].split(" "))  # Guarda em uma lista

        # loop do final dos vertices até o final do arquivo
        for line in range(qtdVertices+2, len(content)):
            arestas.append(content[line].split(" "))   # Guarda em uma lista

        # Cria o grafo com todos os vertices
        g = Grafo(qtdVertices)

        for i in range(qtdVertices-1):  # armazena os nomes
            g.nomes[i] = vertices[i][1].rstrip('\n')

        for i in range(qtdArestas):  # Adiciona todas as arestas e pesos
            g.insereAresta(int(arestas[i][0]), int(
                arestas[i][1]), int(arestas[i][2]))
            
        g.typeGraph = tipoGrafo

        return g

def writeFile(file):
    with open(file, 'w') as f:
        print("Digite as informações do grafo dessejado e 'fim' quando parar: ")
        while True:
            linha = input()
            if linha == 'fim':
                break

            f.write(linha + '\n')

def inserirVertice(graph):
    nomeVertice = input("Informe o nome do vértice: ")
    graph.insereVertice(nomeVertice)

def inserirAresta(graph):
    verticeOrigem = int(input("Vértice de origem: "))
    verticeDestino = int(input("Vértice de destino: "))
    peso = int(input("Peso da aresta: "))
    graph.insereAresta(verticeOrigem, verticeDestino, peso)

def removerVertice(graph):
    vertice = input("Informe a cidade que deseja remover: ")
    idVertice = -1
    print(f"Nome da cidade: {vertice}")
    print(graph.nomes)

    for i in graph.nomes:
        if(graph.nomes[i] == vertice):
            idVertice = i

    if(idVertice == -1):
        print("Cidade não consta no grafo.")

    print(f"idVertice: {idVertice}")
    

def showContent(graph):
        print(f"Número de vértices: {graph.n}.\nNúmero de arestas: {graph.m}")

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
    if len(graph.busca_profundidade(1)) != graph.n-1:
        print("Grafo é desconexo!")
    else:
        print("Grafo é conexo!")


def menu():
    controle = True
    graph = 0
    while(True):
        print('\n\n', "<",  "-"*60, ">")
        print(" |", " "*5, "Mapeamento da rota da seda durante o século XIV", " "*6, "|", "\n", "|", "-"*60, "|", "\n",
            "|", " "*20, "Opções de operações: ", " "*17, "|", "\n", "|", "-"*60, "|", "\n",
            "|", " "*15, "1. Ler os dados do arquivo.", " "*16, "|", "\n", "|", "-"*60, "|", "\n",
            "|", " "*15, "2. Gravar dados no arquivo.", " "*16, "|", "\n", "|", "-"*60, "|", "\n",
            "|", " "*15, "3. Inserir vértice no Grafo.", " "*15, "|", "\n", "|", "-"*60, "|", "\n",
            "|", " "*15, "4. Inserir aresta no Grafo.", " "*16, "|", "\n", "|", "-"*60, "|", "\n",
            "|", " "*15, "5. Mostrar conteúdo do arquivo.", " "*12, "|", "\n", "|", "-"*60, "|", "\n",
            "|", " "*15, "6. Mostrar grafo.", " "*26, "|", "\n", "|", "-"*60, "|", "\n",
            "|", " "*15, "7. Conexidade do grafo.", " "*20, "|", "\n", "|", "-"*60, "|", "\n",
            "|", " "*15, "8. Encerrar.", " "*31, "|", "\n", "<", "-"*60, ">", "\n",
            )
        opcao = int(input("Escolha a opção: "))

        match opcao:
            case 1:
                graph = grafoArq("grafo.txt")
                print("Arquivo lido com sucesso.")
                time.sleep(2)
            case 2:
                fileII = input("Informe o arquivo: ")
                writeFile(fileII)
                time.sleep(2)
            case 3:
                inserirVertice(graph)
                time.sleep(2)
            case 4:
                inserirAresta(graph)
                print("Aresta inserida com sucesso.")
                time.sleep(2)
            case 5:
                print("Conteúdo do arquivo")
                showContent(graph)
                time.sleep(2)
            case 6:
                print("\n\n", "-"*20, "   Apresentação do grafo   ", "-"*20)
                graph.show()
                time.sleep(3)
            case 7:
                print("Conexidade do grafo: ", end="")
                conexidadeGrafo(graph)
                time.sleep(2)
            case 8:
                print("Fim do programa")
                controle = False
                time.sleep(2)
                break
            case _:
                print("Opção inválida!")
                time.sleep(2)



def main():
    menu()


main()