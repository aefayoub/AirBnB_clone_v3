-- Insert data into the states table
INSERT INTO states (id, name, updated_at, created_at)
VALUES ('6', 'California', NOW(), NOW());

-- Insert data into the cities table
INSERT INTO cities (id, state_id, name, updated_at, created_at)
VALUES ('6', '1', 'Los Angeles', NOW(), NOW());

-- Insert data into the users table
INSERT INTO users (id, updated_at, created_at, email, password, first_name, last_name)
VALUES ('6', NOW(), NOW(), 'user@example.com', 'hashed_password', 'John', 'Doe');

-- Insert data into the places table
INSERT INTO places (id, updated_at, created_at, state_id, name, city_id, description, number_rooms, number_bathrooms, max_guest, price_by_night, latitude, longitude, user_id)
VALUES ('6', NOW(), NOW(), '1', 'Beautiful Home', '1', 'A lovely place to stay', 3, 2, 6, 150, 34.0522, -118.2437, '1');

-- Insert data into the reviews table
INSERT INTO reviews (id, updated_at, created_at, user_id, place_id, text)
VALUES ('6', NOW(), NOW(), '1', '1', 'Great place to stay!');

-- Insert data into the amenities table
INSERT INTO amenities (id, updated_at, created_at, name)
VALUES ('6', NOW(), NOW(), 'Wi-Fi');

-- Insert data into the place_amenity table
INSERT INTO place_amenity (amenity_id, place_id)
VALUES ('6', '1');

