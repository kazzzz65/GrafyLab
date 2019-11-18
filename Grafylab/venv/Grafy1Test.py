#w grupie poniedziałkowej numpy było niepotrzebne, ale lepiej użyć.
import numpy as np
from Grafy1Funkcje import *
from random import seed

vertices = ["a", "b", "c", "d", "e"]
matrix = np.array([[0,1,1,0,0],[0,0,1,0,0],[0,0,0,1,1],[0,0,0,0,1],[0,0,0,0,0]])
#poniedziałkowa: matrix = [[0,1,1,0,0],[0,0,1,0,0],[0,0,0,1,1],[0,0,0,0,1],[0,0,0,0,0]]
#aktualne rozwiązanie powinno być lepsze

print(matrix) # wypisuje macierz
print_matrix(vertices,matrix) #wypisuje graf z nazwami wierzchołków
print_matrix([],matrix) #wypisuje graf nazywając wierzchołki liczbami 1,2,...n
print("")

#graf w formie słownika/listy sąsiedztwa - będziemy tę formę preferować.
graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']}
print(graph)
print_graph(graph)
print("")

#graf w formie słownika tworzony od podstaw, krok po kroku
graph = {}
add_arc(graph, ("a", "b"))
add_arc(graph, ("a", "c"))
add_arc(graph, ("b", "c"))
add_arc(graph, ("c", "d"))
add_vertex(graph, "e")
print_graph(graph)
print("")

#graf losowy - wykorzystanie funkcji
#ustawienie tzw. ziarna generatora liczb losowych
#dzięki temu wyniki są powtarzalne (można wstawić inną liczbę)
#brak użycie seed() - wyniki będą nie do powtórzenia
seed(2019)
random_graph = random_graph(10, 1/5)
print_graph(random_graph)
print("")

#graf skierowny z pliku lista.txt (lista łuków)
graph = graph_from_edges("lista.txt", 1)
print_graph(graph)

#zapisany do pliku graf.txt (lista sąsiadów)
graph_to_neighbourslist(graph, "graf.txt")

#wczytany z pliku graf.txt (lista sąsiedów) jako graf nieskierowany
print_graph(graph_from_neighbourslist("graf.txt"))