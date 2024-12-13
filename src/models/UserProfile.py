from database import db_manager

class UserProfile:
    def __init__(self, user_id, name=None, budget=None, dietaryPreference=None):
        self.user_id = user_id
        self.name = name
        self.budget = budget
        self.dietaryPreference = dietaryPreference

    def save_to_db(self):
        conn =