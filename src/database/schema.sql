CREATE TABLE users(
    user_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    budget NUMERIC,
    dietaryPreference TEXT
);

