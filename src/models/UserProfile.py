from psycopg2._psycopg import cursor
from src.database.Db_manager import createConnection

class UserProfile:
    def __init__(self, user_id, name=None, budget=None, dietaryPreference=None):
        self.user_id = user_id
        self.name = name
        self.budget = budget
        self.dietaryPreference = dietaryPreference

    def save_to_db(self):
        conn = createConnection()
        cur = conn.cursor()
        query = """ 
            INSERT INTO users (user_id, name, budget, dietaryPreference)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (user_id) DO UPDATE SET
            name = excluded.name,
            budget = EXCLUDED.budget,
            dietaryPreference = EXCLUDED.dietaryPreference;
        """

        cursor.execute(query, (self.user_id, self.name, self.budget, self.dietaryPreference))
        conn.commit()
        cursor.close()
        conn.close()
        
    @staticmethod
    def get_from_db(user_id):
        conn = createConnection()
        cur = conn.cursor()
        query = "SELECT * FROM users WHERE user_id = %s;"
        cursor.execute(query, (user_id,))
        user_data = cursor.fetchone()
        cursor.close()
        conn.close()
        if user_data:
            return UserProfile(
                user_id=  user_data['user_id'],
                name = user_data['name'],
                budget = user_data['budget'],
                dietaryPreference = user_data['dietaryPreference']
            )
        else:
            return None
    
    def update_budget(self, new_budget):
        self.budget = new_budget
        self.save_to_db()
