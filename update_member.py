from connect_mysql import connect_database  # Import the function to connect to the MySQL database

# Establish a connection to the database
conn = connect_database()

# Check if the connection was successful
if conn is not None:
    try:
        # Create a cursor object to interact with the database
        cursor = conn.cursor()

        # Updated details for the member (age, id)
        updated_member = ("31", 10)  # Tuple containing the new age and the member's id

        # SQL query to update the member's age based on their id
        query = "UPDATE Members SET age = %s WHERE id = %s"

        # Execute the update query with the provided data
        cursor.execute(query, updated_member)

        # Commit the transaction to save changes in the database
        conn.commit()
        print("Member details successfully updated.")  # Confirmation message

    except Exception as e:
        # Handle any exceptions that occur during the update process
        print(f"An error occurred: {e}")
    
    finally:
        # Close the cursor and connection to clean up resources
        cursor.close()
        conn.close()
        print("Connection closed.")  # Confirmation that the connection is closed

