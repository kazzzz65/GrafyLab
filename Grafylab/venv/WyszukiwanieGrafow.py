from Grafy1Funkcje import *
from random import seed

seed(10)
graph = random_graph(15,1/6)
# print_graph(graph)
#
# print("Liczba wierzchołków" , len(graph))
# przeszukiwanie wgłąb
VT=ConnectedComponent(graph)
print(VT)
if len(VT)== len(graph):
    print("Graf jest spójny")
else:
    print("Graf jest niespójny")

print(ConnectedComponents(graph))
if len(VT)<=1:
    print("Graf jest spójny")
else:
    print("Graf jest niespójny")

