import numpy as np


def printMatrix(dane, wierzch):
    n = len(dane)
    if (len(wierzch) < n):
        w = range(n)
    else:
        w = wierzch
    for i in range(n):
        print(w[i], ":", sep="", end="")
        for j in range(n):
            if (dane[i][j] == 1):
                print(' ', w[j], sep="", end="")
        print("")


def printGraph(graph):
    for v in graph:
        print(v, ":", end="")
        for u in graph[v]:
            print(" ", u, end="")
        print("")


def addVertex(graph, vertex):
    """dodaję wierchołek do istniejącego graphu"""
    if vertex not in graph:
        graph[vertex] = []


def addArc(graph, arc):
    """dodaję łuk do grafu"""
    u, v = arc
    addVertex(graph, u)
    addVertex(graph, v)
    if v not in graph[u]:
        graph[u].append(v)


def addEdge(graph, edge):
    u, v = edge
    addVertex(graph, u)
    addVertex(graph, v)
    if u == v:
        raise ValueError("pętla!")
    if v not in graph[u]:
        graph[u].append(v)
    if u not in graph[v]:
        graph[v].append(u)


# zadania domowe
def changeMatrixToList(matrix):
    a = ord('A')
    alph = [chr(i) for i in range(a, a + 26)]
    n = len(matrix)
    for i in range(n):
        print(alph[i], ":", sep="", end="")
        for j in range(n):
            if matrix[i][j] == 1:
                print(" ", alph[j], end="")
        print("")


def changeListToMatrix(list1):
    list1 = dict(list1)
    n = len(list1.keys())
    matrix = np.zeros((n,n))

    vertex1Table = getKeyTable(list1)
    vertex2Table = getValuesTable(list1)

    for i in range(n):
        for j in range(len(vertex2Table[i])):
            if vertex2Table[i][j] in vertex1Table[0]:
                k=vertex1Table[0].index(vertex2Table[i][j])
                matrix[i][k] = 1
    print(np.matrix(matrix))


def getValuesTable(list1):
    vertex2 = str(list(list(list1.values())))
    vertex2 = vertex2.replace("\'", "")
    vertex2 = vertex2.replace(",", "")
    vertex2 = vertex2.replace(" ", "")
    vertex2 = vertex2.replace("[", "")
    vertex2Table = vertex2.split("]")
    return vertex2Table


def getKeyTable(list1):
    vertex1 = str(list(list(list1.keys())))
    vertex1 = vertex1.replace("\'", "")
    vertex1 = vertex1.replace(",", "")
    vertex1 = vertex1.replace(" ", "")
    vertex1 = vertex1.replace("[", "")
    vertex1 = vertex1.replace("]", "")
    vertex1Table = vertex1.split()
    return vertex1Table
