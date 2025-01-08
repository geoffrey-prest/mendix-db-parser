import graph
import logging
import relations

from argparse import Namespace

def main(args: Namespace) -> None:
    logging.info(f"Finding paths from {args.source_table} to {args.target_table} in {args.ddl}")
    relation_map = relations.generate_relation_map_from_sql("doc/example/DDL")
    relation_graph = graph.generate_from_relation_map(relation_map)
    graph.draw_graph(relation_graph)