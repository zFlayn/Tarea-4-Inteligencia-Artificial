import networkx as nx
import random
import time

def generate_graph(n_nodes):
    G = nx.Graph()
    for i in range(n_nodes):
        for j in range(i+1, n_nodes):
            if random.random() > 0.5:
                G.add_edge(i, j, weight=random.randint(1, 5000))
    return G

def bfs_shortest_path(G, start, end):
    visited = set()
    queue = [(start, [start])]
    while queue:
        (node, path) = queue.pop(0)
        if node not in visited:
            visited.add(node)
            if node == end:
                return path
            for neighbor, data in G[node].items():
                weight = data['weight']
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
    return []

def test_shortest_path(n_nodes):
    G = generate_graph(n_nodes)
    print("Grafo:")
    print(G.edges(data=True))
    nodes_list = list(G.nodes())
    start, end = random.sample(nodes_list, 2)
    print(f"Origen: {start}, Destino: {end}")
    start_time = time.time()
    shortest_path = bfs_shortest_path(G, start, end)
    end_time = time.time()
    print(f"Camino más corto: {shortest_path}")
    print(f"Tiempo de ejecución: {end_time - start_time:.8f} segundos")

if __name__ == "__main__":
    test_shortest_path(5000)
