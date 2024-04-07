CREATE TABLE profile (
    id serial PRIMARY KEY,
    username VARCHAR(255) UNIQUE,
    firstname VARCHAR(255),
    lastname VARCHAR(255),
    email VARCHAR(254),
    password VARCHAR(255),
    profile_pic VARCHAR(255),
    phone_number VARCHAR(255)
);