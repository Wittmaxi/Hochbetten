import numpy as np
import networkx as nx
import scipy.linalg as la

def create_triangle_graph():
    """ Create a complete graph with 3 nodes (triangle) """
    G = nx.Graph()
    G.add_edges_from([('a', 'b'), ('b', 'c'), ('c', 'a')])
    return G

def create_path_graph(num_nodes):
    """ Create a path graph with nodes labeled from 'a' to 'b', with intermediate nodes.
        Add self-loop to the last node in the path """
    G = nx.Graph()
    nodes = [chr(97 + i) for i in range(num_nodes)]  # Create nodes labeled a, b, c, ...
    
    # Add edges between consecutive nodes in the path
    for i in range(num_nodes - 1):
        G.add_edge(nodes[i], nodes[i + 1])
    
    # Add a self-loop on the last node (last node = 'c' in the original context)
    last_node = nodes[-1]
    G.add_edge(last_node, last_node)
    G.add_edge(nodes[0], nodes[0])
    
    return G

def cartesian_product_graph(G1, G2):
    """ Returns the Cartesian product of two graphs G1 and G2 """
    return nx.cartesian_product(G1, G2)

def compute_max_eigenvalue(graph):
    """ Compute the largest eigenvalue of the adjacency matrix of the graph """
    A = nx.adjacency_matrix(graph).todense()
    eigenvalues = la.eigvals(A)
    return max(np.real(eigenvalues))

# Main function
def main():
    # First graph is the triangle graph (3 nodes)
    G1 = create_triangle_graph()

    # Second graph: path graph between 'a' and 'b' with user-defined number of intermediate nodes
    for i in range(1, 100):
        G2 = create_path_graph(i)
        G_product = cartesian_product_graph(G1, G2)
        max_eigenvalue = compute_max_eigenvalue(G_product)
        print(f"The maximum eigenvalue of the adjacency matrix is: {max_eigenvalue}")
        print(f"We had {i} nodes")
        if (max_eigenvalue - 4 > 0.0001):
            exit()

    # Cartesian product of both graphs

    # Compute the largest eigenvalue of the adjacency matrix of the product graph


if __name__ == "__main__":
    main()
