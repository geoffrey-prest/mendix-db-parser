import os
import glob

# Read the content of the existing file
with open('C:\\_repos\\mendix-db-parser\\doc\\example\\scripts\\all-ddl.sql', 'r') as file:
    content = file.read()

# Split the content by 'CREATE TABLE' statements
statements = content.split('CREATE TABLE')
statements = [stmt.strip() for stmt in statements if stmt.strip()]

# Directory to save the new files
target_dir = 'C:\\_repos\\mendix-db-parser\\doc\\example\\DDL\\'

# Delete any files in the target directory:
## Get a list of all files in the target directory
files = glob.glob(os.path.join(target_dir, '*'))
## Iterate over the list of files and remove each one
for f in files:
    os.remove(f)

# Create a new file for each statement in all-ddl.sql
database_name = "unknown"
for stmt in statements:


    if 'DATABASE' in stmt: # Create a new file for the 'CREATE DATABASE' statement (note: it is expected to be first in the file)

        # Determine the database name 
        database_name = stmt.split(' ')[2].replace('[', '').replace(']', '').replace(';', '')

        # Determine the file name
        database_file_name = f'{target_dir}{database_name}.Database.sql'

        # Write the statement to the new file
        with open(database_file_name, 'w') as new_file:
            new_file.write(f'{stmt}')

    else: # Create a new file for each 'CREATE TABLE' statement

        # Determine the table name
        table_name = stmt.split('(')[0].strip().split(' ')[0].replace('[', '').replace(']', '')

        # Determine the file name
        table_file_name = f'{target_dir}{table_name}.Table.sql'

        # Write the statement to the new file
        with open(table_file_name, 'w') as new_file:
            new_file.write(f'''USE [{database_name}];

/**** Lorem ipsum dolor 234 #$% ****/

CREATE TABLE {stmt}''')
        