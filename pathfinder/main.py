import argparse
import logging
import pathfinder

# Configure the logging module to display the time, log level, and message
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A pathfinder through Mendix table relations.")
    parser.add_argument("--source-table", type=str, default="customermanagement$customer", help="The source table to start the path from.")
    parser.add_argument("--target-table", type=str, default="productmanagement$category", help="The target table to end the path at.")
    parser.add_argument("--ddl", type=str, default="doc/example/DDL", help="The directory that contains the DDL to parse.")
    args = parser.parse_args()

    # Attenuate the logging level for the matplotlib and PIL modules
    logging.getLogger('matplotlib.font_manager').setLevel(logging.WARNING)
    logging.getLogger('matplotlib.pyplot').setLevel(logging.WARNING)
    logging.getLogger('PIL.PngImagePlugin').setLevel(logging.WARNING)

    pathfinder.main(args)