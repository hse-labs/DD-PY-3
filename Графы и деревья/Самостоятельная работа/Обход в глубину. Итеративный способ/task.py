from typing import Hashable, List
from collections import deque

import networkx as nx


def dfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Функция выполняет обход в глубину и возвращает список узлов в порядке посещения.
    В данной задаче порядок обхода графа левосторонний или правосторонний не важен,
    главное соблюсти порядок обхода в ширину.

    :param g: Граф NetworkX, по которому нужно совершить обход
    :param start_node: Стартовый узел, откуда нужно начать обход
    :return: Список узлов в порядке посещения.
    """
    visited = {node: False for node in g.nodes}
    d = deque()  # вершина стека справа
    path = []

    d.append(start_node)  # поджигаем узел графа
    visited[start_node] = True  # если узел "подожжен", то мы его посещали
    while d:
        current_node = d.pop()  # снимаем узел с вершины стека
        path.append(current_node)
        for neighbor in g[current_node]:  # g[current_node] - смежные узлы
            if not visited[neighbor]:
                d.append(neighbor)  # добавляем узел на вершину стека
                visited[neighbor] = True

    return path
