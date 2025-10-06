# Import any dependencies needed to execute sql queries
# YOUR CODE HERE
from employee_events.sql_execution import QueryMixin

# Define a class called QueryBase
# Use inheritance to add methods
# for querying the employee_events database.
# YOUR CODE HERE
class QueryBase(QueryMixin):
    def __init__(self):
        super().__init__()

        # Create a class attribute called `name`
        # set the attribute to an empty string
        # YOUR CODE HERE
        self.name = ""

    # Define a `names` method that receives
    # no passed arguments
    # YOUR CODE HERE
    def names(self):
        return []

        # Return an empty list
        # YOUR CODE HERE


    # Define an `event_counts` method
    # that receives an `id` argument
    # This method should return a pandas dataframe
    # YOUR CODE HERE
    
    def event_counts(self, id):


        # QUERY 1
        # Write an SQL query that groups by `event_date`
        # and sums the number of positive and negative events
        # Use f-string formatting to set the FROM {table}
        # to the `name` class attribute
        # Use f-string formatting to set the name
        # of id columns used for joining
        # order by the event_date column
        # YOUR CODE HERE
        query_1 = f"""
                    SELECT event_date
                            , SUM(positive_events) positive_events
                            , SUM(negative_events) negative_events
                    FROM {self.name}
                    JOIN employee_events
                        USING({self.name}_id)
                    WHERE {self.name}.{self.name}_id = {id}
                    GROUP BY event_date
                    ORDER BY event_date
                """
        return self.pandas_query(query_1)

    # Define a `notes` method that receives an id argument
    # This function should return a pandas dataframe
    # YOUR CODE HERE
    def notes(self, id):

        query_2 = f"""
                    SELECT note_date
                            , note
                    FROM notes
                    WHERE {self.name}_id = {id}
                """
        return self.pandas_query(query_2)

        # QUERY 2
        # Write an SQL query that returns `note_date`, and `note`
        # from the `notes` table
        # Set the joined table names and id columns
        # with f-string formatting
        # so the query returns the notes
        # for the table name in the `name` class attribute
        # YOUR CODE HERE

if __name__ == "__main__":
    qb = QueryBase()
    qb.name = "employee"
    print(qb.event_counts(1))
    print(qb.notes(1))
