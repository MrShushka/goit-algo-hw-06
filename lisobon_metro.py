import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Завантаження даних з CSV файлів
lines = pd.read_csv('lisbon.lines.csv')
stations = pd.read_csv('lisbon.stations.csv')
connections = pd.read_csv('lisbon.connections.csv')

# Створюємо граф
G = nx.Graph()

# Додаємо вузли (станції)
for _, row in stations.iterrows():
    G.add_node(
        row['id'],
        name=row['name'],
        pos=(row['longitude'], row['latitude'])
    )

# Додаємо ребра (сполучення між станціями)
for _, row in connections.iterrows():
    line_colour = lines[lines['line'] == row['line']]['colour'].values[0]
    G.add_edge(row['station1'], row['station2'], colour=line_colour)

