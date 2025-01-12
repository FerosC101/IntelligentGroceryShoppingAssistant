import unittest
from unittest.mock import patch, MagicMock
from src.models.ShoppingList import ShoppingList


class TestShoppingList(unittest.TestCase):

    @patch('src.database.Db_manager.createConnection')  # Mocking createConnection
    def test_add_and_remove_item(self, mock_create_connection):
        # Mock the database connection and cursor
        mock_conn = mock_create_connection.return_value
        mock_cursor = mock_conn.cursor.return_value

        # Simulate inserting a product into the products table (mocking the constraint)
        mock_cursor.execute.side_effect = lambda query, params: None if "INSERT INTO products" in query else MagicMock()

        # Mock data for the product
        mock_cursor.execute("INSERT INTO products (product_id, name) VALUES (%s, %s);", [101, "Test Product"])

        user_id = 1
        shopping_list = ShoppingList(user_id)

        # Simulate adding an item
        shopping_list.add_item(101, 2)
        mock_cursor.execute.assert_any_call(
            """
            INSERT INTO shopping_list (user_id, product_id, quantity)
            VALUES (%s, %s, %s)
            ON CONFLICT (user_id, product_id) DO UPDATE SET
            quantity = shopping_list.quantity + EXCLUDED.quantity;
            """,
            [user_id, 101, 2]
        )

        # Simulate removing an item
        shopping_list.remove_item(101)
        mock_cursor.execute.assert_any_call(
            "DELETE FROM shopping_list WHERE user_id = %s AND product_id = %s;",
            [user_id, 101]
        )

    @patch('src.database.Db_manager.createConnection')  # Mocking createConnection
    def test_get_items(self, mock_create_connection):
        # Mock the database connection and cursor
        mock_conn = mock_create_connection.return_value
        mock_cursor = mock_conn.cursor.return_value

        user_id = 1
        shopping_list = ShoppingList(user_id)

        # Mock the database response to simulate fetched items
        mock_cursor.execute.return_value = None  # Simulate no exceptions for SELECT
        mock_cursor.fetchall.return_value = [{'product_id': 101, 'quantity': 2}, {'product_id': 102, 'quantity': 5}]

        # Simulate the retrieval of items
        items = shopping_list.get_items()

        # Verify the items were fetched correctly
        self.assertEqual(len(items), 2)
        self.assertEqual(items[0]['product_id'], 101)
        self.assertEqual(items[1]['quantity'], 5)

        mock_cursor.execute.assert_called_with(
            "SELECT product_id, quantity FROM shopping_list WHERE user_id = %s;",
            [user_id]
        )

    def setUp(self):
        # Disable foreign key checks
        mock_conn = patch('src.database.Db_manager.createConnection').start().return_value
        mock_cursor = mock_conn.cursor.return_value
        mock_cursor.execute("PRAGMA foreign_keys = OFF;")  # SQLite example
        # or for MySQL:
        # mock_cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")


if __name__ == "__main__":
    unittest.main()
