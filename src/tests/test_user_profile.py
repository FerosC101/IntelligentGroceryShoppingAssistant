import unittest
from src.models.UserProfile import  UserProfile

class TestUserProfile(unittest.TestCase):
    def setUp(self):
        user_id = UserProfile("test_user", "vegetarian")
        user = UserProfile.get_user(user_id)
        self.assertEqual(user[1], "test_user")
        self.assertEqual(user[2], "vegetarian")

if __name__ == '__main__':
    unittest.main()