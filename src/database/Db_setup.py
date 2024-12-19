import psycopg2

def create_tables():
    conn = psycopg2.connect("dbname=igroceryshopping user=vince password=426999")
    cur = conn.cursor()
    cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                budget NUMERIC,
                dietaryPreference TEXT
            );

            CREATE TABLE IF NOT EXISTS products (
                product_id SERIAL PRIMARY KEY,
                name VARCHAR(100),
                price NUMERIC,
                category VARCHAR(50),
                nutrition_info JSONB
            );

            CREATE TABLE IF NOT EXISTS shopping_list (
                user_id INT REFERENCES users(user_id),
                product_id INT REFERENCES products(product_id),
                quantity INT,
                PRIMARY KEY (user_id, product_id)
            );

            CREATE TABLE IF NOT EXISTS store_products (
                store_id SERIAL,
                product_id INT REFERENCES products(product_id),
                PRIMARY KEY (product_id)
            );
            
            CREATE TABLE IF NOT EXISTS purchases (
            purchase_id SERIAL PRIMARY KEY,
            user_id INT REFERENCES users(user_id),
            product_id INT REFERENCES products(product_id),
            date DATE,
            quantity INT,
            total_price NUMERIC
        );
        """)

    conn.commit()
    cur.close()
    conn.close()

