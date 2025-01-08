import json
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
        nx.write_graphml(graph, "debug/graph.graphml")
        logging.debug("Graph has been stored in 'graph.graphml'.")

    return graph

def find_path(relation_graph, source_table, target_table):
    """
    Finds all paths between a source table and a target table in a relation graph and returns the shortest one.

    Args:
        relation_graph (nx.DiGraph): A directed graph where nodes represent tables and edges represent relationships between them.
        source_table (str): The table to start the path from.
        target_table (str): The table to end the path at.

    Returns:
        List[str]: a list of table names representing the shortest path from the source table to the target table.
    """
    logging.info(f"Finding the shortest path from {source_table} to {target_table}.")

    try:
        all_paths = list(nx.all_simple_paths(relation_graph, source_table, target_table))
        logging.info(f"Found {len(all_paths)} paths.")

        shortest_path = nx.shortest_path(relation_graph, source=source_table, target=target_table)
        logging.info(f"Shortest path from {source_table} to {target_table}: {shortest_path}")
    except nx.NetworkXNoPath:
            logging.warning(f"No path found from {source_table} to {target_table}.")
            return []

    if logging.getLogger().isEnabledFor(logging.DEBUG):
        logging.debug(f"all_paths: {all_paths}")
        with open('debug/all_paths.json', 'w') as file:
            json.dump(all_paths, file, indent=4)
        logging.debug(f"shortest_path: {shortest_path}")
        with open('debug/shortest_path.json', 'w') as file:
            json.dump(shortest_path, file, indent=4)

    return shortest_path

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