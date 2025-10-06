from sqlite3 import connect
from pathlib import Path
from functools import wraps
import pandas as pd

# Using pathlib, create a `db_path` variable
# that points to the absolute path for the `employee_events.db` file
#### YOUR CODE HERE
# the file is locared in the employee_events folder
db_path = Path(__file__).parent / "employee_events.db"
db_path = db_path.resolve()

# OPTION 1: MIXIN
# Define a class called `QueryMixin`
class QueryMixin:

    def __init__(self):
        self.conn = connect(db_path)
        self.sql_cursor = self.conn.cursor()
    
    # Define a method named `pandas_query`
    # that receives an sql query as a string
    # and returns the query's result
    # as a pandas dataframe
    #### YOUR CODE HERE
    def pandas_query(self, sql_query: str):

        df = pd.read_sql_query(sql_query, self.conn, index_col = None)

        return df

    # Define a method named `query`
    # that receives an sql_query as a string
    # and returns the query's result as
    # a list of tuples. (You will need
    # to use an sqlite3 cursor)
    #### YOUR CODE HERE
    def query(self, sql_query: str):
        result = self.sql_cursor.execute(sql_query).fetchall()
        return result

 
 # Leave this code unchanged
def query(func):
    """
    Decorator that runs a standard sql execution
    and returns a list of tuples
    """

    @wraps(func)
    def run_query(*args, **kwargs):
        query_string = func(*args, **kwargs)
        connection = connect(db_path)
        cursor = connection.cursor()
        result = cursor.execute(query_string).fetchall()
        connection.close()
        return result
    
    return run_query

if __name__ == "__main__":
    qm = QueryMixin()
    print(qm.pandas_query("SELECT * FROM employee").head())
    print(qm.query("SELECT * FROM employee"))