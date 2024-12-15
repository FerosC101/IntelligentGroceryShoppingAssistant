from src.database.Db_manager import createConnection

class Product:
    def __init__(self, product_id, name=None, price=None, category=None, nutrition_info=None):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.nutrition_info = nutrition_info
        self.price = price

    def save_to_db(self):
        conn = createConnection()
        cur = conn.cursor()
        query = """
            INSERT INTO products (product_id, name, price, category, nutrition_info)
            VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT (product_id) DO UPDATE SET
            name = EXCLUDED.name,
            price = EXCLUDED.price,
            category = EXCLUDED.category,
            nutrition_info = EXCLUDED.nutrition_info;
        """

        cur.execute(query, (self.product_id, self.name, self.price, self.category, self.nutrition_info))
        conn.commit()
        conn.close()

    @staticmethod
    def get_from_db(product_id):
        conn = createConnection()
        cur = conn.cursor()
        query = "SELECT * FROM products WHERE product_id = %s;"
        cur.execute(query, (product_id,))
        product_data = cur.fetchone()
        conn.close()
        cur.close()
        conn.close()
        if product_data:
            return Product(
                product_id=product_data['product_id'],
                name=product_data['name'],
                price=product_data['price'],
                category=product_data['category'],
                nutrition_info=product_data['nutrition_info']
            )
        return None

