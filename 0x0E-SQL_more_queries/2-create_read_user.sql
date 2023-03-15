-- creates database hbtn_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- creates a new user
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- grants privileges for new user
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
