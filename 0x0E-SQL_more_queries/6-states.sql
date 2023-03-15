-- creates a new database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- creates a new table in database
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
	id INT UNIQUE NOT NULL AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY (id)
);
