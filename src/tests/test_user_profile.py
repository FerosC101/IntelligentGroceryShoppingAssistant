import unittest
from src.models.UserProfile import UserProfile


class TestUserProfile(unittest.TestCase):
    def setUp(self):
        self.test_user = UserProfile.create_user(name="test", dietaryPreference="vegetarian")

    def test_user_creation(self):
        user = UserProfile.get_from_db(self.test_user.user_id)
        self.assertIsNotNone(user)
        self.assertEqual(user.name, "test")
        self.assertEqual(user.dietaryPreference, "vegetarian")

    def test_update_budget(self):
        self.test_user.update_budget(500)
        user = UserProfile.get_from_db(self.test_user.user_id)
        self.assertEqual(user.budget, 500)


if __name__ == '__main__':
    unittest.main()
