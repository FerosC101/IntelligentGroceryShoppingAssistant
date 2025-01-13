import unittest
from src.models.Analytics import Analytics

class TestAnalytics(unittest.TestCase):
    def setUp(self):
        self.analytics = Analytics(user_id=1)

    def test_analyze_spending(self):
        result = self.analytics.analyze_spending()
        self.assertGreaterEqual(result["total_spent"], 0)

    def test_recommend_items(self):
        preferences = ["dairy", "vegetables"]
        recommendations =  self.analytics.recommend_items(preferences)
        self.assertIsInstance(recommendations, list)
        for product in recommendations:
            self.assertTrue(product.category in preferences)

if __name__ == '__main__':
    unittest.main()

