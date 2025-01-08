import relations
#import graph
from typing import Any

def main(args: Any) -> None:
    print(f"Finding paths from {args.source_table} to {args.target_table} in {args.ddl}")
    #relation_map = relations.generate_relation_map_from_sql("doc/example/DDL")
    #table_graph = graph.generate_graph(relation_map)
    # paths = find_all_paths("customermanagement$customer", "productmanagement$category", relation_map)
    # save_paths_to_json(paths, "paths.json")