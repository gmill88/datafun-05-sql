"""Project 5 summary: The purpose of this module is to work with python to interact with an SQL database. 
In the project a database was created and several sql commands were run on it. The project also implemented logging
to enhance debugging and provide a record of program execution
"""

#Import dependencies
import pathlib
import sqlite3
import pandas as pd
import logging
import pandas as pd
import logging 

#configure logging
logging.basicConfig(filename='log.txt', level=logging.DEBUG, filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')
#added to beginning of main method
logging.info("Program started")

db_file = pathlib.Path("project.db")

def create_database():
    """Function to create a database. Connecting for the first time
    will create a new database file if it doesn't exist yet.
    Close the connection after creating the database
    to avoid locking the file."""
    logging.debug("Starting Major Function") #logging the start of major functions
    try:
        conn = sqlite3.connect(db_file)
        conn.close()
        print("Database created successfully.")
    except sqlite3.Error as e:
        print("Error creating the database:", e)
    logging.debug("ending major function")

    
def create_tables():
    """Function to read and execute SQL statements to create tables"""
    logging.debug("Starting Major Function") #logging the end of major functions
    try:
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("sql", "create_tables.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            print("Tables created successfully.")
    except sqlite3.Error as e:
        print("Error creating tables:", e)
    logging.debug("ending major function")


def insert_data_from_csv():
    """Function to use pandas to read data from CSV files (in 'data' folder)
    and insert the records into their respective tables."""
    logging.debug("Starting Major Function")
    try:
        author_data_path = pathlib.Path("data", "authors.csv")
        book_data_path = pathlib.Path("data", "books.csv")
        authors_df = pd.read_csv(author_data_path)
        books_df = pd.read_csv(book_data_path)
        with sqlite3.connect(db_file) as conn:
            # use the pandas DataFrame to_sql() method to insert data
            # pass in the table name and the connection
            authors_df.to_sql("authors", conn, if_exists="replace", index=False)
            books_df.to_sql("books", conn, if_exists="replace", index=False)
            print("Data inserted successfully.")
    except (sqlite3.Error, pd.errors.EmptyDataError, FileNotFoundError) as e:
        print("Error inserting data:", e)
    logging.debug("ending major function")


def execute_sql_from_file(db_filepath, sql_file):
    logging.debug("Starting Major Function")
    with sqlite3.connect(db_filepath) as conn:
        with open(sql_file, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {sql_file}")
    logging.debug("ending major function")


def main():
    logging.debug("Starting Major Function")
    create_database()
    create_tables()
    insert_data_from_csv()
    db_filepath = 'project.db'

    base_path = pathlib.Path()
    
    execute_sql_from_file(db_filepath, 'sql/create_tables.sql')

    insert_data_from_csv()

    execute_sql_from_file(db_filepath, 'sql/insert_records.sql')

    execute_sql_from_file(db_filepath, 'sql/update_records.sql')
    execute_sql_from_file(db_filepath, 'sql/delete_records.sql')
    execute_sql_from_file(db_filepath, 'sql/query_aggregation.sql')
    execute_sql_from_file(db_filepath, 'sql/query_filter.sql')
    execute_sql_from_file(db_filepath, 'sql/query_sorting.sql')
    execute_sql_from_file(db_filepath, 'sql/query_group_by.sql')
    execute_sql_from_file(db_filepath, 'sql/query_join.sql')

    logging.info("all sql operations complete") #logging.info used to log other major events
    logging.debug("ending major function")
#end of main method
logging.info("Program ended")
# Conditional script
if __name__ == '__main__':
    main()