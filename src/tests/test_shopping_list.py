import unittest
from unittest.mock import patch, MagicMock, call
from src.models.ShoppingList import ShoppingList


class TestShoppingList(unittest.TestCase):
    def setUp(self):
        self.db_patcher = patch('src.database.Db_manager.createConnection')
        self.mock_create_connection = self.db_patcher.start()

        self.mock_conn = MagicMock()
        self.mock_cursor = MagicMock()

        self.mock_conn.cursor.return_value = self.mock_cursor
        self.mock_create_connection.return_value = self.mock_conn

        def default_fetchone(*args, **kwargs):
            print("Default fetchone called with:", args, kwargs)
            return [1]

        self.mock_cursor.fetchone = MagicMock(side_effect=default_fetchone)

        self.user_id = 1
        self.shopping_list = ShoppingList(self.user_id)

        print("Setup complete. Mock cursor state:", self.mock_cursor.fetchone.return_value)

    def tearDown(self):
        self.db_patcher.stop()

    def test_add_item(self):
        product_id = 101
        quantity = 2

        print("Initial fetchone mock:", self.mock_cursor.fetchone.return_value)

        def mock_fetchone_side_effect(query=None, params=None):
            print(f"Mock fetchone called with query: {query}, params: {params}")
            return [1]

        self.mock_cursor.fetchone = MagicMock(side_effect=mock_fetchone_side_effect)

        print("Mock state after setup:", self.mock_cursor.fetchone.return_value)

        try:
            self.shopping_list.add_item(product_id, quantity)
        except Exception as e:
            print(f"Exception occurred: {e}")
            print("Mock fetchone was called:", self.mock_cursor.fetchone.called)
            print("Mock fetchone call count:", self.mock_cursor.fetchone.call_count)
            print("Mock fetchone call args:", self.mock_cursor.fetchone.call_args_list)
            raise


    def test_remove_item(self):
        product_id = 101

        self.shopping_list.remove_item(product_id)

        actual_calls = self.mock_cursor.execute.call_args_list

        expected_call = call(
            "DELETE FROM shopping_list WHERE user_id = %s AND product_id = %s;",
            [self.user_id, product_id]
        )

        self.assertIn(expected_call, actual_calls)

    def test_get_items(self):
        mock_items = [
            {'product_id': 101, 'quantity': 2},
            {'product_id': 102, 'quantity': 5}
        ]
        self.mock_cursor.fetchall.return_value = mock_items

        items = self.shopping_list.get_items()

        self.assertEqual(len(items), 2)
        self.assertEqual(items[0]['product_id'], 101)
        self.assertEqual(items[1]['quantity'], 5)

        expected_call = call(
            "SELECT product_id, quantity FROM shopping_list WHERE user_id = %s;",
            [self.user_id]
        )
        self.assertIn(expected_call, self.mock_cursor.execute.call_args_list)

    def test_add_item_with_nonexistent_product(self):
        product_id = 999
        quantity = 1

        self.mock_cursor.fetchone.return_value = None

        with self.assertRaises(Exception):
            self.shopping_list.add_item(product_id, quantity)


if __name__ == "__main__":
    unittest.main()