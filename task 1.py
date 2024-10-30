import networkx as nx
import matplotlib.pyplot as plt
from lisobon_metro import G

# # Створюємо порожній граф
# G = nx.Graph()

# # Додаємо вершини (станції метро)
# stations = [
#     "Station A", "Station B", "Station C", 
#     "Station D", "Station E", "Station F", 
#     "Station G", "Station H"
# ]
# G.add_nodes_from(stations)

# # Додаємо ребра (лінії між станціями)
# edges = [
#     ("Station A", "Station B"),
#     ("Station A", "Station C"),
#     ("Station B", "Station D"),
#     ("Station C", "Station D"),
#     ("Station C", "Station E"),
#     ("Station D", "Station F"),
#     ("Station E", "Station F"),
#     ("Station E", "Station G"),
#     ("Station F", "Station H"),
#     ("Station G", "Station H"),
# ]
# G.add_edges_from(edges)

# Візуалізація графа
plt.figure(figsize=(15, 10))

# Отримуємо позиції вузлів
pos = nx.get_node_attributes(G, 'pos')

# Отримуємо кольори ребер
edges = G.edges(data=True)
edge_colours = [edge[2]['colour'] for edge in edges]

# Малюємо граф
nx.draw(
    G, pos, with_labels=True, node_size=100, font_size=8,
    node_color='skyblue', edge_color=edge_colours, width=2
)

plt.title("Транспортна мережа Лісабона")
plt.show()

# Аналіз графа
print("Кількість станцій (вершин):", G.number_of_nodes())
print("Кількість сполучень (ребер):", G.number_of_edges())

# Ступінь вершин
print("\nСтупінь кожної станції:")
for node, degree in G.degree():
    station_name = G.nodes[node]['name']
    print(f"{station_name}: {degree}")
# Аналіз основних характеристик
print("Кількість вершин:", G.number_of_nodes())
print("Кількість ребер:", G.number_of_edges())
print("\nСтупінь кожної вершини:")
for node, degree in G.degree():
    print(f"{node}: {degree}")

# Діаметр графу
if nx.is_connected(G):
    print("\nДіаметр графу:", nx.diameter(G))
else:
    print("\nГраф не є зв'язним, діаметр не визначений.")
