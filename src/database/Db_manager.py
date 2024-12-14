import psycopg2

def createConnection():
    try:
        connection = psycopg2.connect(
            host = "localhost",
            database = "igroceryshopping",
            user = "vince",
            password = "426999",
            port = "5432"
        )
        return connection
    except Exception as e:
        print(f"Error: {e}")
        return None

def closeConnection(connection):
    if connection:
        connection.close()
        print("Connection closed")

