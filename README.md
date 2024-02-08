# datafun-05-sql

## Project start
1. Start a new repository and select default README.md
2. Clone the repository to local environment. Used VS Code functionality to clone the repository. 
3. Open the project and activate the virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```
4. Install dependencies pyarrow and pandas into the .venv
```bash
python3 -m pip install pandas pyarrow
```
5. Freeze dependencies into requirements.txt
 ```bash
 python3 -m pip freeze > requirements.txt
  ```
6.  Create a .gitignore using the touch commonad and add .venv, .vscode, and .DS_Store

7. Import dependencies at the top of the Project after the introduction. These include
- import pathlib
- import sqlite3
- import pandas as pd
- import logging
- import pandas as pd
- import logging 

8. Use logging throughout the project. 
This example was provided:

```python
import logging

# Configure logging to write to a file, appending new logs to the existing file
logging.basicConfig(filename='log.txt', level=logging.DEBUG, filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Program started") # add this at the beginning of the main method
logging.info("Program ended")  # add this at the end of the main method
```
9. Using the related books and authors csv's design a schema and create a Database

Implement the SQL operations
- create_tables.sql 
- insert_records.sql 
- update_records.sql 
- delete_records.sql
- query_aggregation.sql
- query_filter.sql 
- query_sorting.sql 
- query_group_by.sql 
- query_join.sql 

10. Use python to interact using th commands: 
```python
import sqlite3

def execute_sql_from_file(db_filepath, sql_file):
    with sqlite3.connect(db_filepath) as conn:
        with open(sql_file, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {sql_file}")

```

11. Define the main function for the SQL Operations Script and implement it to execute SQL operations logic

12. Include conditional script execution

13. Git add and commit then push to GitHub
```bash
git add .
git commit -m "initial comment"
git push origin main   
``` 