from typing import Hashable, List
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
    path = []

    def recursion_dfs(current_node):
        visited[current_node] = True
        path.append(current_node)
        for neighbor in g[current_node]:
            if not visited[neighbor]:
                recursion_dfs(neighbor)

    recursion_dfs(start_node)

    return path
