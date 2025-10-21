-- Create the database if it does not already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the created or existing database
USE hbtn_0d_usa;

-- Create the table 'states' if it does not already exist
CREATE TABLE IF NOT EXISTS states (
	-- Unique, auto-generated, not null, primary key
	id INT AUTO_INCREMENT PRIMARY KEY,
	-- Name colum, cannot be null
	name VARCHAR(256) NOT NULL
);
