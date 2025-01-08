import json
import logging
import re
import os

def generate_relation_map_from_sql(directory: str) -> dict:
    """
    Generates a relation map from SQL DDL files in the specified directory.
    This function reads SQL DDL files from the given directory, identifies join tables,
    and constructs a relation map that describes the relationships between tables.
    Args:
        directory (str): The directory containing SQL DDL files.
    Returns:
        dict: A dictionary representing the relation map, where keys are table names
              and values are lists of tuples. Each tuple contains a join table name
              and the related table name.
    Raises:
        FileNotFoundError: If the specified directory does not exist.
        IOError: If there is an error reading a file in the directory.
    """
    logging.info(f"Generating a relation map from SQL DDL files in {directory}")
    relation_map: dict = {}

    tables = get_tables(directory)

    # Pattern to match join tables in SQL DDL files.
    # Assumptions:
    # - Table names and column names follow the pattern \w+\$\w+
    # - Columns are of type int, but this can be adjusted if needed
    # - Whitespace around table and column definitions is optional
    join_table_pattern = re.compile(
        r'CREATE TABLE \[dbo\]\.\[(\w+\$\w+)\]\s*\(\s*\[(\w+\$\w+)\]\s*\[\w+\],\s*\[(\w+\$\w+)\]\s*\[\w+\]\s*\);'
    )
    for filename in os.listdir(directory):
        if filename.endswith('Table.sql'):
            with open(os.path.join(directory, filename), 'r') as file:
                content = file.read()
                matches = join_table_pattern.findall(content)
                for match in matches:
                    table_name = match[0]
                    column1 = match[1]
                    column2 = match[2]
                    table1 = get_table_for_column(column1, tables)
                    table2 = get_table_for_column(column2, tables)
                    if table1 and table2:
                        if table1 not in relation_map:
                            relation_map[table1] = []
                        if table2 not in relation_map:
                            relation_map[table2] = []
                        relation_map[table1].append((table_name, table2))
                        relation_map[table2].append((table_name, table1))
        
    if logging.getLogger().isEnabledFor(logging.DEBUG):
        with open('debug/relation_map.json', 'w') as file:
            json.dump(relation_map, file, indent=4)
    
    return relation_map

def get_tables(directory: str) -> list[str]:
    """
    Extracts and returns a list of table names from SQL DDL files in the specified directory.

    Parameters:
    directory (str): The path to the directory containing SQL DDL files.

    Returns:
    list: A list of table names found in the SQL DDL files.
    """
    tables = []
    table_pattern = re.compile(r'CREATE TABLE \[dbo\]\.\[(\w+\$\w+)\]')
    for filename in os.listdir(directory):
        if filename.endswith('Table.sql'):
            with open(os.path.join(directory, filename), 'r') as file:
                content = file.read()
                tables.extend(table_pattern.findall(content))
    return tables

def get_table_for_column(column_name: str, tables: list[str]) -> str | None:
    """
    Given a column name and a list of tables, return the table that is contained within the column name.

    Args:
        column_name (str): The name of the column to search for.
        tables (list): A list of table names to search within.

    Returns:
        str or None: The name of the table that contains the column, or None if no table is found.
    """
    for table in tables:
        if table in column_name:
            return table
    return None