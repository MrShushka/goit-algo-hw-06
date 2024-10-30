import pandas as pd
import networkx as nx
from collections import deque
from lisobon_metro import G

start_station = 1  # Aeroporto
goal_station = 18  # Marquês de Pombal

def get_path_from_tree(tree, start, goal):
    path = []
    current = goal

    while current != start:
        path.append(current)
        current = list(tree.predecessors(current))[0]

    path.append(start)
    return path[::-1]  


dfs_tree = nx.dfs_tree(G, source=start_station)
dfs_path = get_path_from_tree(dfs_tree, start=start_station, goal=goal_station)

bfs_tree = nx.bfs_tree(G, source=start_station)
bfs_path = get_path_from_tree(bfs_tree, start=start_station, goal=goal_station)

print("Шлях DFS:", [G.nodes[node]['name'] for node in dfs_path])
print("Шлях BFS:", [G.nodes[node]['name'] for node in bfs_path])


print("\nПорівняння:")
print(f"Довжина шляху DFS: {len(dfs_path)}")
print(f"Довжина шляху BFS: {len(bfs_path)}")
