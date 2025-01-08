import logging
import networkx as nx
import matplotlib.pyplot as plt

from typing import Dict, List, Tuple

def generate_from_relation_map(relation_map: Dict[str, List[Tuple[str, str]]]) -> nx.DiGraph:
    """
    Generates a directed graph from a relation map.

    Args:
        relation_map (Dict[str, List[Tuple[str, str]]]): A dictionary where the keys are source table names
        and the values are lists of tuples. Each tuple contains two strings representing an intermediate table
        and a target table.

    Returns:
        nx.DiGraph: A directed graph where nodes represent tables and edges represent relationships between them.
    """
    logging.info(f"Generating a graph from a relation map with {len(relation_map)} tables.")
    graph = nx.DiGraph()
    for source_table, relations in relation_map.items():
        for relation in relations:
            intermediate_table, target_table = relation
            graph.add_edge(source_table, intermediate_table)
            graph.add_edge(intermediate_table, target_table)
    
    if logging.getLogger().isEnabledFor(logging.DEBUG):
        logging.debug(f"Graph has {graph.number_of_nodes()} nodes and {graph.number_of_edges()} edges.")
        logging.debug(f"Graph has {nx.number_strongly_connected_components(graph)} strongly connected components.")
        nx.write_graphml(graph, "graph.graphml")
        logging.debug("Graph has been stored in 'graph.graphml'.")

    return graph

def draw_graph(graph: nx.DiGraph) -> None:
    """
    Draws a directed graph using Matplotlib and NetworkX.

    Parameters:
    graph (nx.DiGraph): A directed graph object from NetworkX.

    Returns:
    None
    """
    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, node_size=3000, node_color='lightblue', font_size=10, font_weight='bold', arrows=True)
    plt.title('Network of Connected Nodes')
    plt.show()