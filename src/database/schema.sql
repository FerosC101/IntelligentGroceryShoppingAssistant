CREATE TABLE users(
    user_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    budget NUMERIC,
    dietaryPreference TEXT
);
DROP TABLE products;
CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    price NUMERIC,
    category VARCHAR(50),
    nutrition_info TEXT
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

INSERT INTO users VALUES (1, 'test_user', 0, 'vegetarian');
INSERT INTO products VALUES (101, 'cinnabon', '10', 'food', '');
INSERT INTO shopping_list VALUES (1, '101', '2');
