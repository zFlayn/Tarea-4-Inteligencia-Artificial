import random
import networkx as nx
import heapq
import time


def generate_graph(n_nodes):
    G = nx.Graph()
    for i in range(n_nodes):
        for j in range(i+1, n_nodes):
            if random.random() > 0.5:
                G.add_edge(i, j, weight=random.randint(1, 60))
    return G


def dijkstra(G, start, end):
    distances = {node: float('inf') for node in G.nodes()}
    distances[start] = 0
    pq = [(0, start)]
    while len(pq) > 0:
        current_distance, current_node = heapq.heappop(pq)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in G[current_node].items():
            distance = current_distance + weight['weight']
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    shortest_path = [end]
    current_node = end
    while current_node != start:
        for neighbor, weight in G[current_node].items():
            if distances[neighbor] + weight['weight'] == distances[current_node]:
                shortest_path.append(neighbor)
                current_node = neighbor
                break
    shortest_path.reverse()
    return shortest_path


def test_shortest_path(n_nodes):
    G = generate_graph(n_nodes)
    print("Grafo:")
    print(G.edges(data=True))
    nodes_list = list(G.nodes())
    start, end = random.sample(nodes_list, 2)
    print(f"Origen: {start}, Destino: {end}")
    start_time = time.time()
    shortest_path = dijkstra(G, start, end)
    end_time = time.time()
    print(f"Camino más corto: {shortest_path}")
    print(f"Tiempo de compilación: {end_time - start_time} segundos")


if __name__ == "__main__":
    test_shortest_path(60)
