from psycopg2.extras import RealDictCursor
from src.database.Db_manager import createConnection

class ShoppingList:
    def __init__(self, user_id):
        self.user_id = user_id

    def get_items(self):
        conn = createConnection()
        cur = conn.cursor(cursor_factory = RealDictCursor)
        query = "SELECT * FROM shopping_list WHERE user_id = %s"
        cur.execute(query, [self.user_id])
        items = cur.fetchall()
        cur.close()
        conn.close()
        return items

    def add_item(self, product_id, quantity):
        conn = createConnection()
        cursor = conn.cursor()

        # Debug: Add print statements
        print(f"Checking existence for product_id: {product_id}")

        cursor.execute("SELECT 1 FROM products WHERE product_id = %s", [product_id])
        result = cursor.fetchone()
        print(f"Query result: {result}")

        if not result:
            cursor.close()
            conn.close()
            raise Exception(f"Product with ID {product_id} does not exist")

        query = """INSERT INTO shopping_list (user_id, product_id, quantity)
            VALUES (%s, %s, %s)
            ON CONFLICT (user_id, product_id) DO UPDATE SET
            quantity = shopping_list.quantity + EXCLUDED.quantity;"""

        cursor.execute(query, [self.user_id, product_id, quantity])
        conn.commit()
        cursor.close()
        conn.close()

    def remove_item(self, product_id):
        conn = createConnection()
        cursor = conn.cursor()
        query = "DELETE FROM shopping_list WHERE user_id = %s AND product_id = %s;"
        cursor.execute(query, [self.user_id, product_id])
        conn.commit()
        cursor.close()
        conn.close()



