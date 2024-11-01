from connect_mysql import connect_database

#Establishing the connection
conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()

        session_date = "2024-01-15"
        member_id = 10
       

        query = "INSERT INTO Workoutsessions (session_date, member_id) VALUES (%s, %s)"

        cursor.execute(query, (session_date, member_id))
        conn.commit()
        print("Workout Added Successfully for John Doe.")

    finally:
        cursor.close()
        conn.close()
        print("Connection closed.")