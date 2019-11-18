# w wersji poniedziałkowej niepotrzebne, tu chyba też nie
from random import random
from typing import Any


def print_matrix(vertices, matrix):
    """wypisuje na ekranie graf podany w formie macierzy sąsiedztwa i nazw wierzchołków"""
    n = len(matrix)
    # w wersji poniedziałkowej był tu równoważny warunek
    if len(vertices) == n:
        w = vertices
    else:
        w = range(1, n + 1)
    for i in range(n):
        print(w[i], ":", end="")
        for j in range(n):
            # w wersji poniedziałkowej if matrix[i][j]
            if matrix[i, j]:
                print(" ", w[j], end="")
        print("")


def print_graph(graph):
    """wypisuje na ekranie graf podany w formie listy sąsiedztwa"""
    for v in graph:
        print(v, ":", end="")
        for u in graph[v]:
            print(" ", u, end="")
        print("")


def add_vertex(graph, vertex):
    """Dodaje wierzchołek do istniejącego grafu"""
    if vertex not in graph:
        graph[vertex] = []


def add_arc(graph, arc):
    """Dodaje łuk (skierowany) do grafu"""
    u, v = arc
    add_vertex(graph, u)
    add_vertex(graph, v)
    if v not in graph[u]:
        graph[u].append(v)


def add_edge(graph, edge):
    """Dodaje krawędź (nieskierowaną) do grafu"""
    u, v = edge
    add_vertex(graph, u)
    add_vertex(graph, v)
    if u == v:
        raise ValueError("Pętla!\n Graf prosty nie może mieć pętli!")
    if v not in graph[u]:
        graph[u].append(v)
    if u not in graph[v]:
        graph[v].append(u)


def random_graph(n, p):
    """Tworzy graf losowy w modelu G(n, p) - graf nieskierowany, n wierzchołków, każda para połączona krawędzią
    niezależnie, z prawdopodobieństwem p"""
    random_graph = {}
    for i in range(1, n + 1):
        add_vertex(random_graph, i)
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if random() <= p:
                add_edge(random_graph, (i, j))
    return random_graph


def graph_from_edges(filename, directed=0):
    """Wczytuje graf z pliku tesktowego który w każdej linii zawiera opis jednej krawędzi (pary słów)
       ewentualnie jednego wierzchołka (pojedyncze słowo). Jako wynik zwraca graf w formie listy/słownika
       Albo plik musi być w katalogu projektu, albo filename musi zawierać pełną ścieżkę."""
    graph = {}  # pusty graf
    file = open(filename, "r")  # otwarcie pliku do odczytu
    for line in file:  # dla każdej linii w pliku
        words = line.split()  # rozbijam linię na słowa (rozdzielone spacjami)
        if len(words) == 1:  # jedno słowo - wierzchołek
            add_vertex(graph, words[0])
        elif len(words) >= 2:  # więcej słów - używam dwóch pierwszych
            if directed:
                add_arc(graph, (words[0], words[1]))
            else:
                print(words)
                print(words[0], words[1])
                add_edge(graph, (words[0], words[1]))
    file.close()
    return graph


def graph_to_neighbourslist(graph, filename):
    """Zapisuje graf jako listę sąsiedztwa w pliku tekstowym filename"""
    file = open(filename, "w")
    for v in graph:
        neigh_list = "{}:".format(v)  # używamy format do budowy napisu - listy sąsiadów na razie postaci 'v:'
        for u in graph[v]:
            neigh_list = neigh_list + " {}".format(u)  # dołączamy u na koniec napisu listy sąsiadów
        neigh_list = neigh_list + '\n'  # koniec wiersza
        file.write(neigh_list)  # zapisujemy wiersz do pliku
    file.close()


def graph_from_neighbourslist(filename, directed=0):
    """Wczytuje graf z pliku tesktowego który w każdej linii zawiera listę sąsiadów jednego wierzchołka
       Jako wynik zwraca graf w formie listy/słownika
       Albo plik musi być w katalogu projektu, albo filename musi zawierać pełną ścieżkę."""
    graph = {}  # pusty graf
    file = open(filename, "r")  # otwarcie pliku do odczytu
    for line in file:  # dla każdej linii w pliku
        words = line.split(':')  # rozbijam linię na części (rozdzielone dwukropkiem)
        if len(words) > 0:  # sprawdzam, czy linia nie była pusta
            u = words[0]  # przed dwukropkiem był wierzchołek
            add_vertex(graph, u)
            if len(words) > 1:  # jest druga część - tam są sąsiedzi rozdzieleni spacjami
                words = words[1].split()  # rozdzielam więc ich
                if directed:  # wariant dla grafów skierowanych lub nie
                    for v in words:  # dla każdego słowa dodaję łuk
                        add_arc(graph, (u, v))
                else:
                    for v in words:  # lub krawędź dla nieskierowanych
                        add_edge(graph, (u, v))
    file.close()
    return graph


def ConnectedComponent(graph):
    # znajduję jedną spójną składową w grafie nieskierowanym
    # Jako wynik zwraca zbiór jej wierzchołków
    def DFS(u):
        for w in graph[u]:
            if w not in VT:
                VT.add(w)
                DFS(w)

    for v in graph:
        break
    VT = set([v])
    DFS(v)
    return VT


def ConnectedComponents(graph):
    # znajduję jedną spójną składową w grafie nieskierowanym
    # Jako wynik zwraca zbiór jej wierzchołków
    def DFS(u, i):
        for w in graph[u]:
            if w not in VT[i]:
                VT[0].add(w)
                VT[i].add(w)
                DFS(w, i)

    VT = [set([])]
    # VT - lista zbiorów, VT[i] - zbiór wierzchołków i-tej spójnej składowej
    # VT - suma_i VT[i]
    i = 0
    for v in graph:
        if v not in VT[0]:
            VT[0].add(v)
            i=i+1
            VT.append(set([v]))
            DFS(v, i)
    return VT

