# Import the function to connect to the MySQL database
from connect_mysql import connect_database

# Establish a connection to the database
conn = connect_database()

# Check if the connection was successful
if conn is not None:
    try:
        # Create a cursor object to interact with the database
        cursor = conn.cursor()

        # Define the SQL query to retrieve sessions for members whose names start with 'Alice'
        query = """
        SELECT s.session_id AS SessionID, s.session_date AS SessionDate, m.id AS MemberID, m.name
        FROM Members m, Workoutsessions s
        WHERE m.id = s.member_id AND m.name LIKE 'Alice%';
        """

        # Execute the SQL query
        cursor.execute(query)

        # Fetch all results from the executed query and print each order
        for order in cursor.fetchall():
            print(order)

    except Exception as e:
        # Print any errors that occur during database operations
        print(f"Error: {e}")

    finally:
        # Close the cursor to free up resources
        cursor.close()
        # Close the database connection
        conn.close()
        # Indicate that the connection has been closed
        print("Connection Closed.")
