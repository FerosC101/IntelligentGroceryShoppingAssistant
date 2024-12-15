CREATE TABLE users(
    user_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    budget NUMERIC,
    dietaryPreference TEXT
);

CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    price NUMERIC,
    category VARCHAR(50),
    nutrition_info JSONB
);

CREATE TABLE shopping_list(
    user_id INT REFERENCES users(user_id),
    product_id INT REFERENCES products(product_id),
    quantity INT,
    PRIMARY KEY (user_id, product_id)
);

CREATE TABLE store_products (
    store_id SERIAL,
    product_id INT REFERENCES products(product_id),
    PRIMARY KEY (product_id)
);