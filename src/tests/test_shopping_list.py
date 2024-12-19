import unittest
from unittest.mock import patch, MagicMock
from src.models.ShoppingList import ShoppingList


class TestShoppingList(unittest.TestCase):

    @patch('src.database.Db_manager.createConnection')  # Mocking createConnection
    def test_add_and_remove_item(self, mock_create_connection):
        # Mock the database connection and cursor
        mock_conn = mock_create_connection.return_value
        mock_cursor = mock_conn.cursor.return_value

        user_id = 1
        shopping_list = ShoppingList(user_id)

        # Simulate adding an item (no actual DB operation)
        shopping_list.add_item(101, 2)
        mock_cursor.execute.assert_called_with(
            """
            INSERT INTO shopping_list (user_id, product_id, quantity)
            VALUES (%s, %s, %s)
            ON CONFLICT (user_id, product_id) DO UPDATE SET
            quantity = shopping_list.quantity + EXCLUDED.quantity;
            """,
            [user_id, 101, 2]
        )

        # Simulate removing an item (no actual DB operation)
        shopping_list.remove_item(101)
        mock_cursor.execute.assert_called_with(
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
        mock_cursor.fetchall.return_value = [{'product_id': 101, 'quantity': 2}, {'product_id': 102, 'quantity': 5}]

        # Simulate the retrieval of items
        items = shopping_list.get_items()

        # Verify the items were fetched correctly
        self.assertEqual(len(items), 2)
        self.assertEqual(items[0]['product_id'], 101)
        self.assertEqual(items[1]['quantity'], 5)


if __name__ == "__main__":
    unittest.main()