import pandas as pd
import networkx as nx
from lisobon_metro import G
import random

for (u, v) in G.edges():
    G[u][v]['weight'] = random.randint(1, 10)

def dijkstra(graph, start):
    # Ініціалізація відстаней та множини невідвіданих вершин
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.nodes())

    while unvisited:
        # Знаходження вершини з найменшою відстанню серед невідвіданих
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        # Якщо поточна відстань є нескінченністю, то ми завершили роботу
        if distances[current_vertex] == float('infinity'):
            break

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight['weight']

            # Якщо нова відстань коротша, то оновлюємо найкоротший шлях
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        # Видаляємо поточну вершину з множини невідвіданих
        unvisited.remove(current_vertex)

    return distances

for node in G.nodes():
    print(f"\nНайкоротші шляхи від {G.nodes[node]['name']}:")
    all_lengths = dijkstra(G, node)
    for station, length in all_lengths.items():
        print(f"{G.nodes[station]['name']}: {length} хвилин")



