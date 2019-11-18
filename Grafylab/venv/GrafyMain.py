import numpy as np
from random import random
from Grafy1 import *

wierzch=['A','B','C','D','E']
dane = [[0,1,1,0,0],[0,0,1,1,1],[0,0,0,1,0],[0,0,0,0,0],[0,0,1,1,0]]
graph = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}
print(graph)
printGraph(graph)
print("")
addArc(graph, ('A','F'))
addArc(graph, ('A','G'))
addVertex(graph,'H')
printGraph(graph)
print("")
n= 10
p=1/5
randomGraph= {}
# losuję G(n,p)
for i in range(1,n+1):
    addVertex(randomGraph, i)
    for j in range(i+1, n+1):
        if random()<p:
            addEdge(randomGraph, (i,j))
printGraph(randomGraph)

#zadania domowe
print("\n Zadanie domowe nr 1 \n")
changeMatrixToList(dane)
print("\n Zadanie domowe nr 2 \n")
changeListToMatrix(graph)
