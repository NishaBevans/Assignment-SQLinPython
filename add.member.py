from connect_mysql import connect_database

conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()
        
        #New member details
        new_member = "10", "John Doe", "32"

        #SQL query
        query = "INSERT INTO Members (id, name, age) VALUES (%s, %s, %s)"

        #Executing the query
        cursor.execute(query, new_member)
        conn.commit()
        print("New member successfully added to system.")

    finally:
        cursor.close()
        conn.close()
        print ("Connection Closed")