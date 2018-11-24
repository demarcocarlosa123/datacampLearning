import networkx as nx
import matplotlib.pyplot as plt

G = nx.MultiDiGraph()

#Armo los vectores con sus pesos.
G.add_weighted_edges_from([('A', 'B', 3),
                           ('B', 'C', 5),
                           ('C', 'B', 1),
                           ('B', 'E', 1),
                           ('E', 'F', 8)])

print(G.nodes())
print(G.edges())

#Definiendo el color de los nodos
color_map={
    'B':0.6,
    'E':0.4
}
color_default = 1
listColNodes = [color_map.get(node, color_default) for node in G.nodes()]
print(listColNodes)

#Seteo de labels de cada vector, según su peso
dictLabels = dict([((d,h), w['weight']) for d, h, w in G.edges(data=True)])
print(dictLabels)

pos=nx.spring_layout(G)
nx.draw_networkx_edge_labels(G, pos, edge_labels=dictLabels)
nx.draw(G, pos, node_color=listColNodes, node_size=1500, with_labels=True)
plt.draw()
plt.show()

