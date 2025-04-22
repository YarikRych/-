import math

#def dejkstra(graph, start):
#    # Инициализация расстояний и посещённых вершин
#    distances = {vertex: math.inf for vertex in graph}
#    distances[start] = 0
#    visited = set()
#    priority_queue = [(0, start)]  # (расстояние, вершина)
#
#    while priority_queue:
#        current_distance, current_vertex = min(priority_queue)  # получаю вершину с минимальным расстоянием
#        priority_queue.remove((current_distance, current_vertex))  # удаляю её из очереди
#
#        if current_vertex in visited:
#            continue
#
#        visited.add(current_vertex)
#
#        for neighbor, weight in graph[current_vertex]:
#            distance = current_distance + weight
#
#            if distance < distances[neighbor]:
#                distances[neighbor] = distance
#                priority_queue.append((distance, neighbor))  # добавляю соседей в очередь
#
#    return distances
#
#
## Пример графа в виде списков смежности
#graph = {
#    0: [(1, 4), (2, 1)],
#    1: [(3, 1)],
#    2: [(1, 2), (3, 5)],
#    3: []
#}
#
#start_vertex = 0
#distances = dejkstra(graph, start_vertex)
#
#print("Кратчайшие расстояния от вершины", start_vertex)
#for vertex, distance in distances.items():
#    print(f"Вершина {vertex}: {distance}")

def bellman_ford(graph, start):
    # Инициализация расстояний
    distances = {vertex: math.inf for vertex in graph}
    distances[start] = 0

    for _ in range(len(graph) - 1):
        for vertex in graph:
            for neighbor, weight in graph[vertex]:
                if distances[vertex] + weight < distances[neighbor]:
                    distances[neighbor] = distances[vertex] + weight

    # Проверка на наличие отрицательных циклов
    for vertex in graph:
        for neighbor, weight in graph[vertex]:
            if distances[vertex] + weight < distances[neighbor]:
                raise ValueError("Граф содержит отрицательный цикл")

    return distances


# Пример графа в виде списков смежности
graph_bf = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5)],
    3: []
}

start_vertex_bf = 0
distances_bf = bellman_ford(graph_bf, start_vertex_bf)

print("Кратчайшие расстояния от вершины", start_vertex_bf)
for vertex, distance in distances_bf.items():
    print(f"Вершина {vertex}: {distance}")


def visualize_graph(graph, shortest_paths, start):
    with open("graph.dot", "w") as f:
        f.write("digraph G {\n")
        for vertex in graph:
            for neighbor, weight in graph[vertex]:
                f.write(f"    {vertex} -> {neighbor} [label={weight}];\n")

        # Выделяем кратчайшие пути
        for vertex in shortest_paths:
            if shortest_paths[vertex] != math.inf and vertex != start:
                f.write(f"    {start} -> {vertex} [color=red];\n")

        f.write("}\n")

visualize_graph(graph_bf, distances_bf, start_vertex_bf)
