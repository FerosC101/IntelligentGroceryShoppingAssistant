from psycopg2.extras import RealDictCursor
from unicodedata import category

from src.database.Db_manager import createConnection
from src.models.Product import Product


class Analytics:
    def __init__(self, user_id):
        self.user_id = user_id

    def analyze_spending(self):
        conn = createConnection()
        cursor = conn.cursor()
        query = """
        SELECT SUM(p.price * sl.quantity) AS total_spent
        FROM shopping_list sl
        JOIN products p ON sl.product_id = p.product_id
        WHERE sl.user_id = %s;
        """
        cursor.execute(query, (self.user_id,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return {"total_spent": result[0] if result[0] else 0}

    def recommend_items(self, preferences):
        conn = createConnection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        query = """
        SELECT * FROM products
        WHERE category = ANY(%s)
        ORDER BY price ASC;
        """
        cursor.execute(query, (preferences,))
        recommendations = cursor.fetchall()
        cursor.close()
        conn.close()
        return [Product(**rec) for rec in recommendations]

    @staticmethod
    def predict_price(self, base_price=None, season=None):
        seasonal_trends = {"summer": 1.1, "winter": 0.9}
        return {category: base_price * seasonal_trends.get(season, 1)}

