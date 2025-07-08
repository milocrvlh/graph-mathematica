import networkx as nx

G = nx.read_gml("atividade_2/lesmis.gml")

# print(f"O número de nós é {G.number_of_nodes()} e o número de arestas é {G.number_of_edges()}.")

graus = nx.degree(G)
somatorio = 0

for nome, grau in graus:
    somatorio += grau

grau_medio = somatorio / G.number_of_nodes()

print(f"O diâmetro do grafo é {nx.diameter(G)} e o grau médio é {grau_medio:.2f}.")