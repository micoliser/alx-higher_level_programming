-- creates a table second table and inserts multiple rows
CREATE TABLE IF NOT EXISTS second_table (
	id INT,
	name VARCHAR(256),
	score INT
);
-- inserts first row
INSERT INTO second_table
VALUES (1, 'John', 10);
-- inserts second row
INSERT INTO second_table
VALUES (2, 'Alex', 3);
-- inserts third row
INSERT INTO second_table
VALUES (3, 'Bob', 14);
-- inserts fourth row
INSERT INTO second_table
VALUES (4, 'George', 8);
