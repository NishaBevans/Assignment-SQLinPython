from connect_mysql import connect_database

#Establishing the connections
conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()

        #Member to be removed
        customer_to_remove = (10, )

        #SQL query
        query = "DELETE FROM Members WHERE id = %s"

        #Executing the query
        cursor.execute(query, customer_to_remove)
        conn.commit()
        print("Member removed successfully.")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        cursor.close()
        conn.close()
        print("Connection closed.")