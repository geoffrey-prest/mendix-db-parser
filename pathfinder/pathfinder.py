import graph
import logging
import relations

from argparse import Namespace

def main(args: Namespace) -> None:
    """
    Main function to find and log paths between source and target tables in a database schema.
    Args:
        args (Namespace): Command-line arguments containing source_table, target_table, and ddl.
    Returns:
        None
    The function performs the following steps:
    1. Logs the start of the pathfinding process.
    2. Generates a relation map from the provided SQL DDL file.
    3. Creates a graph from the relation map.
    4. Finds a path between the source and target tables.
    5. Logs the found path.
    6. Optionally draws the graph if debug logging is enabled.
    """
    logging.info(f"Finding paths from {args.source_table} to {args.target_table} in {args.ddl}")
    relation_map = relations.generate_relation_map_from_sql("doc/example/DDL")
    relation_graph = graph.generate_from_relation_map(relation_map)
    path = graph.find_path(relation_graph, args.source_table, args.target_table)
    logging.info(f"Path from {args.source_table} to {args.target_table}: {path}")
        
    if logging.getLogger().isEnabledFor(logging.DEBUG):
        graph.draw_graph(relation_graph)