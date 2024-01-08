create table IF NOT EXISTS states(
   id VARCHAR(60) NOT NULL,
   name VARCHAR(128) NOT NULL,
   updated_at DATETIME,
   created_at DATETIME,
   PRIMARY KEY ( id )
);

create table IF NOT EXISTS cities(
   id VARCHAR(60) NOT NULL,
   state_id VARCHAR(60) NOT NULL,
   name VARCHAR(128) NOT NULL,
   updated_at DATETIME,
   created_at DATETIME,
   PRIMARY KEY ( id ),
   CONSTRAINT fk_city_state_id
   FOREIGN KEY (state_id) 
   REFERENCES states(id)
);

create table IF NOT EXISTS places(
   id VARCHAR(60) NOT NULL,
   updated_at DATETIME,
   created_at DATETIME,
   state_id VARCHAR(60) NOT NULL,
   name VARCHAR(128) NOT NULL,
   city_id VARCHAR(60) NOT NULL,
   description VARCHAR(128),
   number_rooms INT NOT NULL DEFAULT 0,
   number_bathrooms INT NOT NULL DEFAULT 0,
   max_guest INT NOT NULL DEFAULT 0,
   price_by_night INT NOT NULL DEFAULT 0,
   latitude DOUBLE,
   longitude DOUBLE,
   PRIMARY KEY ( id ),
   CONSTRAINT fk_place_state_id
   FOREIGN KEY (state_id) 
   REFERENCES states(id),
   CONSTRAINT fk_place_city_id
   FOREIGN KEY (city_id) 
   REFERENCES states(id)
);

create table IF NOT EXISTS amenities(
   id VARCHAR(60) NOT NULL,
   updated_at DATETIME,
   created_at DATETIME,
   name VARCHAR(128),
   PRIMARY KEY ( id )
);

create table IF NOT EXISTS users(
   id VARCHAR(60) NOT NULL,
   updated_at DATETIME,
   created_at DATETIME,
   email VARCHAR(128) NOT NULL,
   password VARCHAR(128) NOT NULL,
   first_name VARCHAR(128),
   last_name VARCHAR(128),
   PRIMARY KEY ( id )
);

create table IF NOT EXISTS reviews(
   id VARCHAR(60) NOT NULL,
   updated_at DATETIME,
   created_at DATETIME,
   user_id VARCHAR(60) NOT NULL,
   place_id VARCHAR(60) NOT NULL,
   text VARCHAR(1024),
   PRIMARY KEY ( id ),
   CONSTRAINT fk_review_user_id
   FOREIGN KEY (user_id) 
   REFERENCES users(id),
   CONSTRAINT fk_review_place_id
   FOREIGN KEY (place_id) 
   REFERENCES places(id)
);

create table IF NOT EXISTS place_amenity(
   amenity_id VARCHAR(60) NOT NULL,
   place_id VARCHAR(60) NOT NULL,
   CONSTRAINT fk_place_amenity_amenity_id
   FOREIGN KEY (amenity_id) 
   REFERENCES amenities(id),
   CONSTRAINT fk_place_amenity_place_id
   FOREIGN KEY (place_id) 
   REFERENCES places(id)
);

-- First, add the user_id column to the places table
ALTER TABLE places
ADD COLUMN user_id VARCHAR(60) NOT NULL;

-- Then, add the foreign key constraint
ALTER TABLE places
ADD CONSTRAINT fk_place_user_id
FOREIGN KEY (user_id) 
REFERENCES users(id);
