#import graph
import logging
import relations

from argparse import Namespace

def main(args: Namespace) -> None:
    logging.info(f"Finding paths from {args.source_table} to {args.target_table} in {args.ddl}")
    relation_map = relations.generate_relation_map_from_sql("doc/example/DDL")
    #table_graph = graph.generate_graph(relation_map)
    # paths = find_all_paths("customermanagement$customer", "productmanagement$category", relation_map)
    # save_paths_to_json(paths, "paths.json")