class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Количество вершин
        self.graph = [[] for _ in range(vertices)]  # Список смежности

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def is_safe(self, v, color, c):
        for neighbor in self.graph[v]:
            if color[neighbor] == c:
                return False
        return True

    def graph_coloring_util(self, m, color, v):
        if v == self.V:
            return True

        for c in range(1, m + 1):
            if self.is_safe(v, color, c):
                color[v] = c

                if self.graph_coloring_util(m, color, v + 1):
                    return True

                color[v] = 0  # Backtrack

        return False

    def graph_coloring(self, m):
        color = [0] * self.V
        if not self.graph_coloring_util(m, color, 0):
            print("Невозможно раскрасить граф с", m, "цветами.")
            return False

        print("Решение раскраски графа:", color)
        self.generate_graphviz_file(color)
        return True

    def generate_graphviz_file(self, color):
        with open("graph_coloring.dot", "w") as f:
            f.write("graph G {\n")
            for v in range(self.V):
                f.write(f'    {v} [label="{v}", style=filled, fillcolor="{self.get_color_name(color[v])}"];\n')
            for u in range(self.V):
                for v in self.graph[u]:
                    if u < v:  # Чтобы не дублировать рёбра
                        f.write(f'    {u} -- {v};\n')
            f.write("}\n")

    def get_color_name(self, color):
        # Возвращает имя цвета в зависимости от номера цвета
        colors = ["white", "red", "green", "blue", "yellow", "orange", "purple", "cyan", "magenta"]
        return colors[color % len(colors)]


if __name__ == "__main__":
    # Создание графа
    g = Graph(9)  # Пример графа с 9 вершинами
    edges = [
        (0, 1), (0, 2), (0, 3),
        (1, 2), (1, 4), (1, 5),
        (2, 3), (2, 6),
        (3, 7),
        (4, 5), (4, 8),
        (5, 6),
        (6, 7),
        (7, 8)
    ]

    for u, v in edges:
        g.add_edge(u, v)

    m = 4  # Количество цветов для раскраски

    print("Решение задачи о раскраске графа методом поиска с возвратом:")
    g.graph_coloring(m)






