from psycopg2.extras import RealDictCursor

from src.database.Db_manager import createConnection
from src.models.Product import Product


class GroceryStore:
    def __init__(self, store_id, name):
        self.store_id = store_id
        self.name = name


    def add_product(self, product):
        conn = createConnection()
        cur = conn.cursor()
        query ="""
            INSERT INTO store_products (store_id, product_id)
            VALUES (%s, %s)
            ON CONFLICT DO NOTHING;
        """

        cur.execute(query, (self.store_id, product.id))
        conn.commit()
        conn.close()

    def get_product_list(self):
        conn = createConnection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        query = """
        SELECT p.* FROM products p
        JOIN store_products sp ON p.product_id = sp.product_id
        WHERE sp.store_id = %s;
        """
        cursor.execute(query, (self.store_id,))
        products = cursor.fetchall()
        cursor.close()
        conn.close()
        return [Product(**product) for product in products]
