import numpy as np
import networkx as nx
import scipy.linalg as la
import itertools


# TODO: function name into english
# TODO: write tests
def random_sprungtreuer_graph_from(matrix):
    (r, c) = matrix.shape
    if r != c:
        raise ValueError(f"{matrix} needs to be a square matrix")

    G = nx.Graph()
    m = matrix.max()
    reg_graphs = []

    for i in range(r):
        # minimal number of nodes needed for the k regular graph i
        n = max(matrix[:, i].tolist())
        k = matrix[i][i]

        if k == n:
            n += 1

        # k * n needs to be even, required by random_regular_graph
        k += (n * k) % 2

        reg = nx.random_regular_graph(matrix[i][i], n)

        new_labels = {}
        for v in range(n):
            new_labels[v] = (i * m) + v

        # prepare the graphs for combining
        reg = nx.relabel_nodes(reg, new_labels)
        reg_graphs.append(reg.nodes())

        G = nx.compose(G, reg)

    for x in range(r):
        for y in range(r):
            if x == y:
                continue
            a = matrix[x][y]
            start_nodes = list(reg_graphs[x])
            end_nodes = list(reg_graphs[y])[:a]
            edges = list(itertools.product(start_nodes, end_nodes))

            G.add_edges_from(edges)

    return G
