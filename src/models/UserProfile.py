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
                name = EXCLUDED.name,
                budget = EXCLUDED.budget,
                dietaryPreference = EXCLUDED.dietaryPreference;
        """
        cur.execute(query, (self.user_id, self.name, self.budget, self.dietaryPreference))
        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def get_from_db(user_id):
        conn = createConnection()
        cur = conn.cursor()
        query = "SELECT * FROM users WHERE user_id = %s;"
        cur.execute(query, (user_id,))
        user_data = cur.fetchone()
        cur.close()
        conn.close()
        if user_data:
            return UserProfile(
                user_id=user_data[0],
                name=user_data[1],
                budget=user_data[2],
                dietaryPreference=user_data[3]
            )
        return None

    @staticmethod
    def create_user(name, dietaryPreference):
        conn = createConnection()
        cur = conn.cursor()
        query = """
            INSERT INTO users (name, dietaryPreference)
            VALUES (%s, %s)
            RETURNING user_id;
        """
        cur.execute(query, (name, dietaryPreference))
        user_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        return UserProfile(user_id=user_id, name=name, dietaryPreference=dietaryPreference)

    @staticmethod
    def get_user(user_id):
        conn = createConnection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE user_id = %s;", (user_id,))
        user = cur.fetchone()
        cur.close()
        conn.close()
        return user

    def update_budget(self, new_budget):
        self.budget = new_budget
        self.save_to_db()

    def __repr__(self):
        return f"<UserProfile(user_id={self.user_id}, name={self.name}, budget={self.budget}, dietaryPreference={self.dietaryPreference})>"
